from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray_1d import getVectorArray_1d


def plot_velocity_1d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin1, xmax1, datatype, axis = 1, point1 = 0.5, point2 = 0.5, file_name = "velocity_1d_window.png", out_dir = ""):
    c = 2.998E10
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, axis, point1, point2)

    minV = np.amin(V)
    maxV = np.amax(V)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[0]
        x = dx * range(V.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[0]
        x = dx * range(V.shape[0]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / V.shape[0]
        x = dx * range(V.shape[0]) + xmin
    else:
        print("wrong axis")
        return
    ax.set_xlabel(r'$z~cm$', fontsize=20)
    ax.set_ylabel(r'$v/c$', fontsize=20)
    #ax.set_yscale("log")
    ax.minorticks_on()
    ax.set_xlim([xmin1, xmax1])
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V, linewidth = 4)

    #plt.show()
    plt.savefig(out_dir + file_name)
    plt.close()