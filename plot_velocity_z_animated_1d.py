from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_velocity_z_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'velocity_z_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5):
    f1 = plt.figure(figsize=[10,8])
    c = 2.998E10
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(ntot, varNames=['vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Vz = getScalarArray_1d(D.vx3, UNIT_VELOCITY / c, axis, point1, point2)

    minV = np.amin(Vz)
    maxV = np.amax(Vz)

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vz.shape[0]
        x = dx * range(Vz.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vz.shape[1]
        x = dx * range(Vz.shape[1]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Vz.shape[2]
        x = dx * range(Vz.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    startOffset = 0

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i + startOffset, varNames=['vx3'], w_dir=w_dir, datatype=datatype)
        Vz = getScalarArray_1d(D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
        if (np.amin(Vz) < minV):
            minV = np.amin(Vz)
        if (np.amax(Vz) > maxV):
            maxV = np.amax(Vz)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([minV, maxV])
        D = pp.pload(frame_number + startOffset, varNames=['vx3'], w_dir=w_dir, datatype=datatype)
        Vx = getScalarArray_1d(D.vx3, UNIT_VELOCITY / c, axis, point1, point2)

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