from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_x_1d(number, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)
    ax.set_yscale("log")

    D = pp.pload(number, varNames = ['vx1'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V=D.vx1.T
    minRho = np.amin(V)
    maxRho = np.amax(V)

    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length * (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0])
    ax.set_ylabel(r'P',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V)

    #plt.show()
    plt.savefig('velocity_x_1d.png')
