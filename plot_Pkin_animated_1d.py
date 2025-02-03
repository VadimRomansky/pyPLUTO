from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_Pkin_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'Pkin_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 200
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['Pkin'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Rho = getScalarArray_1d(D.Pkin, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin
    startOffset = 0

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['Pkin'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.Pkin, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
        if (np.amin(Rho) < minRho):
            minRho = np.amin(Rho)
        if (np.amax(Rho) > maxRho):
            maxRho = np.amax(Rho)

    minRho = maxRho*1E-100

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minRho, 1.1*maxRho])
        D = pp.pload(frame_number, varNames=['Pkin'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.Pkin, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$n_{CR}~cm^{-3}$', fontsize=40, fontweight='bold')
        ax.set_yscale("log")
        ax.minorticks_on()

        im2 = plt.plot(x, Rho)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()