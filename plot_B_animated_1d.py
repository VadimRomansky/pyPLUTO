from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray_1d import getVectorArray_1d


def plot_B_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    # f1 = plt.figure(figsize=[10,8])
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    B = getVectorArray_1d(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), axis, point1, point2)

    minB = np.amin(B)
    maxB = np.amax(B)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / B.shape[0]
    x = dx * range(B.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        B = getVectorArray_1d(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), axis, point1, point2)
        if (np.amin(B) < minB):
            minB = np.amin(B)
        if (np.amax(B) > maxB):
            maxB = np.amax(B)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minB, 1.1*maxB])
        D = pp.pload(frame_number, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        B = getVectorArray_1d(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), axis, point1, point2)

        ax.set_xlabel(r'x', fontsize=18)
        ax.set_ylabel(r'B', fontsize=18)
        ax.minorticks_on()

        im2 = plt.plot(x, B)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"B_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
