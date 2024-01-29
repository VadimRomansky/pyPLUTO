from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_particles_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    f1 = plt.figure(figsize=[8,12])

    P = pr.ploadparticles(0, w_dir=w_dir, datatype='dbl',ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
    maxU = 0
    if(len(PVmag) > 0):
        maxU = max(PVmag)
    index = 0
    for i in range(ntot+1):
        P = pr.ploadparticles(i, w_dir=w_dir, datatype='dbl', ptype='CR')
        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude
        if(len(PVmag) > 0):
            u = max(PVmag)
            if(u > maxU):
                maxU = u
                index = i

    P = pr.ploadparticles(index, w_dir=w_dir, datatype='dbl', ptype='CR')
    PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)

    particles = np.zeros((len(P.x1), 2))
    for i in range(len(particles)):
        particles[i][0] = P.x1[i]
        particles[i][1] = P.x2[i]

    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'],w_dir=w_dir, datatype='dbl') # Load fluid data.
    V = np.sqrt(D.vx1.T ** 2 + D.vx2.T ** 2 + D.vx3.T ** 2)
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    ymin = D.x2.min() * UNIT_LENGTH
    ymax = D.x2.max() * UNIT_LENGTH
    #plt.axis([0.0,1.0,0.0,1.0])


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        cax1 = f1.add_axes([0.91, 0.12, 0.03, 0.75])
        cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        P = pr.ploadparticles(frame_number, w_dir=w_dir, datatype='dbl',
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude

        particles = np.zeros((len(P.x1), 2))
        for i in range(len(particles)):
            particles[i][0] = P.x1[i]
            particles[i][1] = P.x2[i]

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        ax.set_title('Number of particles = ' + str(len(particles)))
        im1 = ax.scatter(particles[:,0], particles[:,1], s=10, c=PVmag, cmap=plt.get_cmap('hot'))  # scatter plot
        #plt.colorbar(im1, cax=cax1)  # vertical colorbar for particle data.
        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
        V = np.sqrt(D.vx1.T ** 2 + D.vx2.T ** 2 + D.vx3.T ** 2)
        im2 = ax.imshow(V, origin='upper', aspect = 'auto',
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        #plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        #time.sleep(1)
        return im1

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"./animate_func.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
