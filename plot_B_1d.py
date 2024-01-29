from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_B_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0

    nx = D.Bx1.shape[0]
    B = np.zeros([nx])

    if (ndim == 1):
        Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 2):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 3):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        zpoint = math.floor(D.Bx1.shape[2] / 2)
        Bz = D.Bx3[:,ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

    minB = np.amin(B)
    maxB = np.amax(B)

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / B.shape[0]
    x = dx * range(B.shape[0]) + xmin
    ax.set_ylabel(r'B',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, B)

    #plt.show()
    plt.savefig('B_1d.png')
