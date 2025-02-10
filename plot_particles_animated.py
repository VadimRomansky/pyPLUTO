from matplotlib import animation
import matplotlib.colors as colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray import getVectorArray


def plot_particles_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'particles.gif', excl_axis = 3, point = 0.5, aspect = 'equal', out_dir = ""):
    f1 = plt.figure(figsize=[10,10])
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams['axes.linewidth'] = 0.1

    P = pr.ploadparticles(0, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
    maxU = 0
    if(len(PVmag > 0)):
        max(PVmag)
    index = 0
    for i in range(ntot+1):
        P = pr.ploadparticles(i, w_dir, datatype=datatype, ptype='CR')
        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude
        if(len(PVmag) > 0):
            u = max(PVmag)
            if(u > maxU):
                maxU = u
                index = i
    if(maxU <= 0):
        maxU = 1
    #index = 27
    P = pr.ploadparticles(index, w_dir, datatype=datatype, ptype='CR')
    PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)

    particles = np.zeros((len(P.x1), 2))
    for i in range(len(particles)):
        particles[i][0] = P.x1[i]*UNIT_LENGTH
        particles[i][1] = P.x2[i]*UNIT_LENGTH

    D = pp.pload(ntot, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.Bx1.shape[0]
    ny = D.Bx1.shape[1]
    B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)

    minB = np.amin(B)
    maxB = np.amax(B)

    for i in range(ntot + 1):
        D = pp.pload(i, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
        B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        if (np.amin(B) < minB):
            minB = np.amin(B)
        if (np.amax(B) > maxB):
            maxB = np.amax(B)

    print("maxB = ", maxB)
    print("minB = ", minB)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    ymin = D.x2.min() * UNIT_LENGTH
    ymax = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        cax1 = f1.add_axes([0.91, 0.12, 0.03, 0.75])
        cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        P = pr.ploadparticles(frame_number, w_dir, datatype=datatype,
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude

        particles = np.zeros((len(P.x1), 2))
        for i in range(len(particles)):
            particles[i][0] = P.x1[i]*UNIT_LENGTH
            particles[i][1] = P.x2[i]*UNIT_LENGTH
            
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        ax.set_title('Number of particles = ' + str(len(particles)))
        im1 = ax.scatter(particles[:,0], particles[:,1], s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin = 0, vmax = maxU)  # scatter plot
        plt.colorbar(im1, cax=cax1)  # vertical colorbar for particle data.
        D = pp.pload(frame_number, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
        B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        #V=D.rho.T
        im2 = ax.imshow(B, origin='upper', norm=colors.Normalize(vmin=minB, vmax=maxB), aspect = aspect,
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.

        return im1

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = out_dir + file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
