from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_temperature_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['T'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0

    nx = D.T.shape[0]
    T = np.zeros([nx])

    if (ndim == 1):
        T = D.T[:]
    if (ndim == 2):
        ypoint = math.floor(D.T.shape[1] / 2)
        T = D.T[:, ypoint]
    if (ndim == 3):
        ypoint = math.floor(D.T.shape[1] / 2)
        zpoint = math.floor(D.T.shape[2] / 2)
        T = D.T[:,ypoint, zpoint]

    minT = np.amin(T)
    maxT = np.amax(T)

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / T.shape[0]
    x = dx * range(T.shape[0]) + xmin
    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$T$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, T)

    #plt.show()
    plt.savefig('temperature_1d.png')
