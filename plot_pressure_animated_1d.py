from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_pressure_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'pressure_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure()
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(ntot, varNames=['prs'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

    minPrs = np.amin(Prs)
    maxPrs = np.amax(Prs)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / Prs.shape[0]
    x = dx * range(Prs.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
        if (np.amin(Prs) < minPrs):
            minPrs = np.amin(Prs)
        if (np.amax(Prs) > maxPrs):
            maxPrs = np.amax(Prs)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minPrs, 1.1*maxPrs])
        D = pp.pload(frame_number, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$P~g~cm^{-1}~s^{-2}$', fontsize=40, fontweight='bold')
        ax.set_yscale("log")
        ax.minorticks_on()

        im2 = plt.plot(x, Prs)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()