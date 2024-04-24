from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_profile(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R', fontsize=18)
    ax.set_ylabel(r'Vx', fontsize=18)
    ax.set_yscale('log')
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, axis, point1, point2)
    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[1]
        x = dx * range(Rho.shape[1]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[2]
        x = dx * range(Rho.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    im2 = plt.plot(x, V, 'r-', x, Prs, 'g-', x, Rho, 'b-')  # plotting fluid data.
    ax.legend(['vx', 'pressure', 'density'])
    plt.savefig('profile.png')
    plt.close()
