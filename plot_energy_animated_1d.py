import numpy as np
from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_energy_animated_1d(ntot, w_dir, unit_density, unit_length, unit_velocity, datatype):
    f1 = plt.figure(figsize=[10, 8])

    D = pp.pload(ntot, varNames = ['rho','vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    density = D.rho.T * unit_density
    nx = density.shape[0]
    vel = np.zeros([nx])
    gam = np.zeros([nx])
    energy = np.zeros([nx])
    r = D.x1
    for i in range(nx):
        vel[i] = np.sqrt(D.vx1.T[i] ** 2 + D.vx2.T[i] ** 2 + D.vx3.T[i] ** 2)
        gam[i] = 1.0 / np.sqrt(1.0 - vel[i] * vel[i] * unit_velocity * unit_velocity / 9E20)
        energy[i] = density[i] * (gam[i] - 1.0) * r[i] * r[i]
    minE = energy[0]
    maxE = energy[0]
    xmin = D.x1.min() * unit_length
    xmax = D.x1.max() * unit_length
    dx = (xmax - xmin) / density.shape[0]
    x = dx * range(density.shape[0])
    startOffset = 0

    for i in range(ntot - startOffset + 1):

        D = pp.pload(i + startOffset, varNames = ['rho','vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        density = D.rho.T * unit_density
        nx = density.shape[0]
        vel = np.zeros([nx])
        gam = np.zeros([nx])
        energy = np.zeros([nx])
        r = D.x1
        for i in range(nx):
            vel[i] = np.sqrt(D.vx1.T[i] ** 2 + D.vx2.T[i] ** 2 + D.vx3.T[i] ** 2)
            gam[i] = 1.0 / np.sqrt(1.0 - vel[i] * vel[i] * unit_velocity * unit_velocity / 9E20)
            energy[i] = density[i] * (gam[i] - 1.0) * r[i] * r[i]
        if (np.amin(energy) < minE):
            minE = np.amin(energy)
        if (np.amax(energy) > maxE):
            maxE = np.amax(energy)

    minE = 0.000000001*maxE
    print(minE, maxE)


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        # ax.set_xlim([xmin, xmax])
        # ax.set_ylim([ymin, ymax])
        ax.set_ylim([minE, maxE])
        ax.set_yscale("log")
        D = pp.pload(frame_number + startOffset, varNames = ['rho','vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        density = D.rho.T * unit_density
        nx = density.shape[0]
        vel = np.zeros([nx])
        gam = np.zeros([nx])
        energy = np.zeros([nx])
        r = D.x1
        for i in range(nx):
            vel[i] = np.sqrt(D.vx1.T[i] ** 2 + D.vx2.T[i] ** 2 + D.vx3.T[i] ** 2)
            gam[i] = 1.0 / np.sqrt(1.0 - vel[i] * vel[i] * unit_velocity * unit_velocity / 9E20)
            energy[i] = density[i] * (gam[i] - 1.0) * r[i] * r[i]

        im2 = plt.plot(x, energy)  # plotting fluid data.
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"energy_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
