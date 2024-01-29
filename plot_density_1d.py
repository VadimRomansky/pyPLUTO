from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.rho.shape))

    minRho = 0
    maxRho = 0

    nx = D.rho.shape[0]
    Rho = np.zeros([nx])

    if (ndim == 1):
        Rho = D.rho[:] * UNIT_DENSITY
    if (ndim == 2):
        ypoint = math.floor(D.rho.shape[1] / 2)
        Rho = D.rho[:, ypoint] * UNIT_DENSITY
    if (ndim == 3):
        ypoint = math.floor(D.rho.shape[1] / 2)
        zpoint = math.floor(D.rho.shape[2] / 2)
        Rho = D.rho[:,ypoint, zpoint] * UNIT_DENSITY

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin
    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$\rho~g~cm^{-3}$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, Rho)

    #plt.show()
    plt.savefig('density_1d.png')
