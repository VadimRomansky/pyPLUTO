from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray_1d import getVectorArray_1d


def plot_velocity_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'velocity_1d_series.png', axis = 1, point1 = 0.5, point2 = 0.5):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    V3 = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, axis, point1, point2)
    D = pp.pload(int(number/2), varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V2 = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
    D = pp.pload(0, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V1 = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)


    minV = min(np.amin(V1), np.amin(V2), np.amin(V3))
    maxV = max(np.amax(V1), np.amax(V2), np.amax(V3))

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V1.shape[0]
        x = dx * range(V1.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V1.shape[0]
        x = dx * range(V1.shape[0]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V1.shape[0]
        x = dx * range(V1.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$B~G$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V1,'b', linewidth = 4)
    plt.plot(x, V2,'g', linewidth = 4)
    plt.plot(x, V3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig(file_name)
    plt.close()