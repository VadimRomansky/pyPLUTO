from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_temperature_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'temperature_1d.gif', axis = 1, point1 = 0.5, point2 = 0.5, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure()
    plt.rcParams["figure.dpi"] = 200

    D = pp.pload(ntot, varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    T = getScalarArray_1d(D.T, 1.0, axis, point1, point2)

    minT = np.amin(T)
    maxT = np.amax(T)

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[0]
        x = dx * range(T.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[0]
        x = dx * range(T.shape[0]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[0]
        x = dx * range(T.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    startOffset = 0

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i+startOffset, varNames=['T'], w_dir=w_dir, datatype=datatype)
        T = getScalarArray_1d(D.T, 1.0, axis, point1, point2)
        if (np.amin(T) < minT):
            minT = np.amin(T)
        if (np.amax(T) > maxT):
            maxT = np.amax(T)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minT, 1.1*maxT])
        D = pp.pload(frame_number+startOffset, varNames=['T'], w_dir=w_dir, datatype=datatype)
        T = getScalarArray_1d(D.T, 1.0, axis, point1, point2)

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$T$', fontsize=40, fontweight='bold')
        ax.minorticks_on()

        im2 = plt.plot(x, T)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = out_dir + file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
