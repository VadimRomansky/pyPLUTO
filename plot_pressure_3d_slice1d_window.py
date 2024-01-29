from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_pressure_3d_slice1d_window(number, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)
    ax.set_yscale("log");

    D = pp.pload(number, varNames = ['prs'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
    zpoint = math.floor(D.prs.T.shape[0] / 2)
    ypoint = math.floor(D.prs.T.shape[1] / 2)
    V = D.prs.T[zpoint, ypoint, :] * unit_density * unit_velocity * unit_velocity
    minRho = np.amin(V)
    maxRho = np.amax(V)

    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length * (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin*unit_length
    ax.set_ylabel(r'P',fontsize=18)
    ax.minorticks_on()
    N1 = int(0.125 * V.shape[0])
    N2 = int(0.275 * V.shape[0])
    x1 = x[N1:N2]
    V1 = V[N1:N2]
    minRho = np.amin(V1)
    maxRho = np.amax(V1)
    im2 = plt.plot(x1, V1)  # plotting fluid data.

    #plt.show()
    plt.savefig('pressure_3d_slice1d_window.png')
