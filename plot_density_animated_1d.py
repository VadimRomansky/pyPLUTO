from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_density_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['rho'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
        if (np.amin(Rho) < minRho):
            minRho = np.amin(Rho)
        if (np.amax(Rho) > maxRho):
            maxRho = np.amax(Rho)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minRho, 1.1*maxRho])
        D = pp.pload(frame_number, varNames=['rho'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$\rho~g~cm^{-3}$', fontsize=40, fontweight='bold')
        ax.set_yscale("log")
        ax.minorticks_on()

        im2 = plt.plot(x, Rho)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"density_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
