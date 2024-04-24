from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_particles_animated_cyl(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, datatype):
    f1 = plt.figure(figsize=[10,8])
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

    #index = 27
    P = pr.ploadparticles(index, w_dir, datatype=datatype, ptype='CR')
    PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)

    particles = np.zeros((len(P.x1), 2))
    for i in range(len(particles)):
        particles[i][0] = P.x1[i]*cos(P.x3[i])*UNIT_LENGTH
        particles[i][1] = P.x1[i]*sin(P.x3[i])*UNIT_LENGTH


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        cax1 = f1.add_axes([0.91, 0.12, 0.03, 0.75])
        P = pr.ploadparticles(frame_number, w_dir, datatype=datatype,
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude

        particles = np.zeros((len(P.x1), 2))
        for i in range(len(particles)):
            particles[i][0] = P.x1[i]*cos(P.x3[i])*UNIT_LENGTH
            particles[i][1] = P.x1[i]*sin(P.x3[i])*UNIT_LENGTH

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([xmin, xmax])
        ax.set_title('Number of particles = ' + str(len(particles)))
        im1 = ax.scatter(particles[:,0], particles[:,1], s=10, c=PVmag, cmap=plt.get_cmap('hot'))  # scatter plot
        plt.colorbar(im1, cax=cax1)  # vertical colorbar for particle data.
        return im1

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"./particles_cyl.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
