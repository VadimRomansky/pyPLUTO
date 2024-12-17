from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_entropy_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'entropy_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 200
    f1 = plt.figure()
    gam = 5.0/3.0

    D = pp.pload(ntot, varNames=['rho','prs'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

    nx = Rho.shape[0]

    S = np.zeros([nx])
    for i in range(nx):
        S[i] = Prs[i] * pow(Rho[i], gam)

    minS = np.amin(S)
    maxS = np.amax(S)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['rho','prs'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
        S = np.zeros([nx])
        for i in range(nx):
            S[i] = Prs[i] * pow(Rho[i], gam)
        if (np.amin(S) < minS):
            minS = np.amin(S)
        if (np.amax(S) > maxS):
            maxS = np.amax(S)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minS, 1.1*maxS])
        D = pp.pload(frame_number, varNames=['rho','prs'], w_dir=w_dir, datatype=datatype)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
        S = np.zeros([nx])
        for i in range(nx):
            S[i] = Prs[i] * pow(Rho[i], gam)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$\rho~g~cm^{-3}$', fontsize=40, fontweight='bold')
        ax.set_yscale("log")
        ax.minorticks_on()

        im2 = plt.plot(x, S)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
