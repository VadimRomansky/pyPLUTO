from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_velocity_x_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'vleocity_x_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5):
    f1 = plt.figure(figsize=[10,8])
    c = 2.998E10
    plt.rcParams["figure.dpi"] = 200

    D = pp.pload(ntot, varNames=['vx1'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Vx = getScalarArray_1d(D.vx1, UNIT_VELOCITY / c, axis, point1, point2)

    minV = np.amin(Vx)
    maxV = np.amax(Vx)

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vx.shape[0]
        x = dx * range(Vx.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vx.shape[0]
        x = dx * range(Vx.shape[0]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vx.shape[0]
        x = dx * range(Vx.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    startOffset = 0

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i + startOffset, varNames=['vx1'], w_dir=w_dir, datatype=datatype)
        Vx = getScalarArray_1d(D.vx1, UNIT_VELOCITY / c, axis, point1, point2)
        if (np.amin(Vx) < minV):
            minV = np.amin(Vx)
        if (np.amax(Vx) > maxV):
            maxV = np.amax(Vx)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([minV, maxV])
        D = pp.pload(frame_number + startOffset, varNames=['vx1'], w_dir=w_dir, datatype=datatype)
        Vx = getScalarArray_1d(D.vx1, UNIT_VELOCITY / c, axis, point1, point2)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$T$', fontsize=40, fontweight='bold')
        ax.minorticks_on()

        im2 = plt.plot(x, Vx)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()