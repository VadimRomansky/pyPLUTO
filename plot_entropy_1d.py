from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_entropy_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'entropy_1d.png', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    gam = 5.0/3.0

    D = pp.pload(ntot, varNames = ['rho','prs'], w_dir = w_dir, datatype=datatype) # Load fluid data.

    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

    nx = Rho.shape[0]

    S = np.zeros([nx])
    for i in range(nx):
        S[i] = Prs[i]/pow(Rho[i], gam)

    minS = np.amin(S)
    maxS = np.amax(S)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$S$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    ax.set_yscale("log")
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, S)

    #plt.show()
    plt.savefig(file_name)
    plt.close()