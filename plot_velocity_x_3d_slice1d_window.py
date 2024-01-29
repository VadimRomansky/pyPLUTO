from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_x_3d_slice1d_window(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R',fontsize=18)
    ax.set_ylabel(r'Vx',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    
    D = pp.pload(ntot, varNames = ['vx1'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.vx1.T.shape[0] / 2)
    ypoint = math.floor(D.vx1.T.shape[1] / 2)
    V = D.vx1.T[zpoint, ypoint, :]
    minRho = 0
    maxRho = V[0]
    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length*(xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0]) + xmin*unit_length
    N1 = int(0.125 * V.shape[0])
    N2 = int(0.275 * V.shape[0])
    x1 = x[N1:N2]
    V1 = V[N1:N2]

    im2 = plt.plot(x1, V1)  # plotting fluid data.
    plt.savefig('velocity_x_3d_slice1d_window.png')
