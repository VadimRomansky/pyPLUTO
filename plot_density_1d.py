from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_density_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'density_1d.png', axis = 1, point1 = 0.5, point2 = 0.5, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype=datatype) # Load fluid data.

    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

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

    ax.set_xlabel(r'$z~cm$', fontsize=20)
    ax.set_ylabel(r'$\rho~g~cm^{-3}$')
    ax.minorticks_on()
    ax.set_yscale("log")
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, Rho, linewidth = 4)

    #plt.show()
    plt.savefig(out_dir + file_name)
    plt.close()
