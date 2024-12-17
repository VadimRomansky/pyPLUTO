from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_temperature_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'temperature_1d_series.png', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(number, varNames = ['T'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    T3 = getScalarArray_1d(D.T, 1.0, axis, point1, point2)
    D = pp.pload(int(number/2), varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    T2 = getScalarArray_1d(D.T, 1.0, axis, point1, point2)
    D = pp.pload(0, varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    T1 = getScalarArray_1d(D.T, 1.0, axis, point1, point2)

    minT = min(np.amin(T1), np.amin(T2), np.amin(T3))
    maxT = max(np.amax(T1), np.amax(T2), np.amax(T3))

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T1.shape[0]
        x = dx * range(T1.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T1.shape[0]
        x = dx * range(T1.shape[0]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T1.shape[0]
        x = dx * range(T1.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$T$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, T1,'b', linewidth = 4)
    plt.plot(x, T2,'g', linewidth = 4)
    plt.plot(x, T3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig(file_name)
    plt.close()