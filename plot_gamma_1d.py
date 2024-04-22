from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray_1d import getVectorArray_1d


def plot_gamma_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis, point1, point2):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.

    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, axis, point1, point2)
    gamma = 1/np.sqrt(1 + np.square(V))

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

    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$\rho~g~cm^{-3}$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    ax.set_yscale("log")
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, gamma)

    #plt.show()
    plt.savefig('gamma_1d.png')
