from matplotlib import animation
import matplotlib.colors as colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray import getScalarArray
from getVectorArray import getVectorArray


def plot_particles_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, background = 'density', file_name = 'particles.gif', excl_axis = 3, point = 0.5, aspect = 'equal'):
    c = 2.998E10
    f1 = plt.figure(figsize=[10,10])

    P = pr.ploadparticles(0, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
    maxU = 0
    minU = 0
    if(len(PVmag > 0)):
        maxU = amax(PVmag)
        minU = amin(PVmag)
    for i in range(ntot+1):
        P = pr.ploadparticles(i, w_dir, datatype=datatype, ptype='CR')
        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude
        if(len(PVmag) > 0):
            u = amax(PVmag)
            if(u > maxU):
                maxU = u
            u = amin(PVmag)
            if(u < minU):
                minU = u

    if(maxU <= 0):
        maxU = 1

    particles = np.zeros((len(P.x1), 2))
    for i in range(len(particles)):
        particles[i][0] = P.x1[i]*UNIT_LENGTH
        particles[i][1] = P.x2[i]*UNIT_LENGTH

    print("minU = ", minU)
    print("maxU = ", maxU)

    backGroundVariable = 0

    if(background == 'density'):
        D = pp.pload(0, varNames=['rho'], w_dir=w_dir, datatype=datatype)
        backGroundVariable = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
    elif(background == 'velocity'):
        D = pp.pload(0, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)
        backGroundVariable = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)
    elif(background == 'pressure'):
        D = pp.pload(0, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        backGroundVariable = getScalarArray(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, excl_axis, point)
    elif(background == 'B'):
        D = pp.pload(0, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        backGroundVariable = getVectorArray(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
    elif(background == 'T'):
        D = pp.pload(0, varNames=['T'], w_dir=w_dir, datatype=datatype)
        backGroundVariable = getScalarArray(D.T, 1.0, excl_axis, point)
    else :
        print('unknown background variable in particle plot')
        return


    minB = np.amin(backGroundVariable)
    maxB = np.amax(backGroundVariable)

    for i in range(ntot + 1):
        if (background == 'density'):
            D = pp.pload(i, varNames=['rho'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
        elif (background == 'velocity'):
            D = pp.pload(i, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, excl_axis, point)
        elif (background == 'pressure'):
            D = pp.pload(i, varNames=['prs'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, excl_axis, point)
        elif (background == 'B'):
            D = pp.pload(i, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getVectorArray(D.Bx1, D.Bx2, D.Bx3,
                                                np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY),
                                                excl_axis, point)
        elif (background == 'T'):
            D = pp.pload(i, varNames=['T'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.T, 1.0, excl_axis, point)
        else:
            print('unknown background variable in particle plot')
            return
        if (np.amin(backGroundVariable) < minB):
            minB = np.amin(backGroundVariable)
        if (np.amax(backGroundVariable) > maxB):
            maxB = np.amax(backGroundVariable)

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

        backGroundVariable = 0
        if (background == 'density'):
            D = pp.pload(frame_number, varNames=['rho'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
        elif (background == 'velocity'):
            D = pp.pload(frame_number, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, excl_axis, point)
        elif (background == 'pressure'):
            D = pp.pload(frame_number, varNames=['prs'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, excl_axis, point)
        elif (background == 'B'):
            D = pp.pload(frame_number, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getVectorArray(D.Bx1, D.Bx2, D.Bx3,
                                                np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY),
                                                excl_axis, point)
        elif (background == 'T'):
            D = pp.pload(frame_number, varNames=['T'], w_dir=w_dir, datatype=datatype)
            backGroundVariable = getScalarArray(D.T, 1.0, excl_axis, point)
        else:
            print('unknown background variable in particle plot')
            return
        #V=D.rho.T
        im2 = ax.imshow(backGroundVariable, origin='upper', norm=colors.Normalize(vmin=minB, vmax=maxB), aspect = aspect,
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.

        im1 = ax.scatter(particles[:, 0], particles[:, 1], s=10, c=PVmag, cmap=plt.get_cmap('hot'), vmin=minU,
                         vmax=maxU)  # scatter plot
        plt.colorbar(im1, cax=cax1)  # vertical colorbar for particle data.

        return im1

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
