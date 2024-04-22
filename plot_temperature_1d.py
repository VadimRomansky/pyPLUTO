from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_temperature_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['T'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    T = getScalarArray_1d(D.T, 1.0, axis, point1, point2)

    minT = np.amin(T)
    maxT = np.amax(T)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[0]
        x = dx * range(T.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[1]
        x = dx * range(T.shape[1]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / T.shape[2]
        x = dx * range(T.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$T$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    ax.set_yscale("log")
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, T)

    #plt.show()
    plt.savefig('temperature_1d.png')
