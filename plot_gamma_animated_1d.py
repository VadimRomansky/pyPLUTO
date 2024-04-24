from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray_1d import getVectorArray_1d


def plot_gamma_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    # f1 = plt.figure(figsize=[10,8])
    c = 2.998E10
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
    gamma = 1 / np.sqrt(1 + np.square(V))

    minV = np.amin(gamma)
    maxV = np.amax(gamma)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[0]
        x = dx * range(V.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[1]
        x = dx * range(V.shape[1]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[2]
        x = dx * range(V.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)
        V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
        gamma = 1 / np.sqrt(1 + np.square(V))
        if (np.amin(gamma) < minV):
            minV = np.amin(gamma)
        if (np.amax(gamma) > maxV):
            maxV = np.amax(gamma)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minV, 1.1*maxV])
        D = pp.pload(frame_number, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)
        V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
        gamma = 1 / np.sqrt(1 + np.square(V))

        ax.set_xlabel(r'x', fontsize=18)
        ax.set_ylabel(r'v/c', fontsize=18)
        ax.set_yscale("log")
        ax.minorticks_on()

        im2 = plt.plot(x, gamma)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"gamma_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
