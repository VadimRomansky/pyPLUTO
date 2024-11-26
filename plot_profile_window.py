from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_profile_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, datatype, file_name = 'profile_window', axis = 1, point1 = 0.5, point2 = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[10, 8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R', fontsize=18)
    ax.set_ylabel(r'Vx', fontsize=18)
    ax.set_yscale('log')
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, axis, point1, point2)
    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

    if (axis == 1):
        xmin1 = D.x1.min() * UNIT_LENGTH
        xmax1 = D.x1.max() * UNIT_LENGTH
        dx = (xmax1 - xmin1) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin1
    elif (axis == 2):
        xmin1 = D.x2.min() * UNIT_LENGTH
        xmax1 = D.x2.max() * UNIT_LENGTH
        dx = (xmax1 - xmin1) / Rho.shape[1]
        x = dx * range(Rho.shape[1]) + xmin1
    elif (axis == 3):
        xmin1 = D.x3.min() * UNIT_LENGTH
        xmax1 = D.x3.max() * UNIT_LENGTH
        dx = (xmax1 - xmin1) / Rho.shape[2]
        x = dx * range(Rho.shape[2]) + xmin1
    else:
        print("wrong axis")
        return

    N1 = 0
    N2 = V.shape[0]

    for i in range(V.shape[0]):
        if (x[i] > xmin):
            N1 = i
            break

    for i in range(V.shape[0]):
        if (x[i] > xmax):
            N2 = i
            break

    x1 = x[N1:N2]
    V1 = V[N1:N2]
    Prs1 = Prs[N1:N2]
    Rho1 = Rho[N1:N2]

    im2 = plt.plot(x1, V1, 'r-', x1, Prs1, 'g-', x1, Rho1, 'b-')  # plotting fluid data.
    ax.legend(['vx', 'pressure', 'density'])
    plt.savefig(file_name)
    plt.close()
