from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_distribution_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    f1 = plt.figure(figsize=[8,12])

    P = pr.ploadparticles(0, w_dir=w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
    maxU = 0
    if(len(PVmag) > 0):
        maxU = max(PVmag)
    index = 0
    for i in range(ntot+1):
        P = pr.ploadparticles(i, w_dir=w_dir, datatype=datatype, ptype='CR')
        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude
        if(len(PVmag) > 0):
            u = max(PVmag)
            if(u > maxU):
                maxU = u
                index = i

    minU = 1E3
    P = pr.ploadparticles(index, w_dir=w_dir, datatype=datatype, ptype='CR')
    PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)

    particles = np.zeros((len(P.x1), 2))
    for i in range(len(particles)):
        particles[i][0] = P.x1[i]
        particles[i][1] = P.x2[i]


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim([1E3,1E8])
        ax.set_ylim([1, 1E5])
        P = pr.ploadparticles(frame_number, w_dir=w_dir, datatype=datatype,
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude


        logP = np.log10(PVmag)
        y, x = np.histogram(PVmag, 1000, range=(minU, maxU + 1), density=False)

        x = x[0:len(x) - 1]

        im1 = ax.plot(x, y)

        return im1

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"./distribution.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
