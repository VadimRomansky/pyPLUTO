from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    c = 2.998E10
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0

    nx = D.vx1.shape[0]
    V = np.zeros([nx])

    if (ndim == 1):
        Vz = D.vx3[:] * UNIT_VELOCITY / c
        Vy = D.vx2[:] * UNIT_VELOCITY / c
        Vx = D.vx1[:] * UNIT_VELOCITY / c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        Vz = D.Vx3[:, ypoint] * UNIT_VELOCITY / c
        Vy = D.Vx2[:, ypoint] * UNIT_VELOCITY / c
        Vx = D.Vx1[:, ypoint] * UNIT_VELOCITY / c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        zpoint = math.floor(D.vx1.shape[2] / 2)
        Vz = D.vx3[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint, zpoint] * UNIT_VELOCITY / c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))

    minV = np.amin(V)
    maxV = np.amax(V)

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin
    ax.set_ylabel(r'v/c',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V)

    #plt.show()
    plt.savefig('velocity_1d.png')
