from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_pressure_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['prs'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.prs.shape))

    minPrs = 0
    maxPrs = 0

    nx = D.prs.shape[0]
    Prs = np.zeros([nx])

    if (ndim == 1):
        Prs = D.prs[:] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 2):
        ypoint = math.floor(D.prs.shape[1] / 2)
        Prs = D.prs[:, ypoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 3):
        ypoint = math.floor(D.prs.shape[1] / 2)
        zpoint = math.floor(D.prs.shape[2] / 2)
        Prs = D.prs[:,ypoint, zpoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY

    minPrs = np.amin(Prs)
    maxPrs = np.amax(Prs)

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / Prs.shape[0]
    x = dx * range(Prs.shape[0]) + xmin
    ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$P~g~cm^{-1}~s^{-2}$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, Prs)

    #plt.show()
    plt.savefig('pressure_1d.png')
