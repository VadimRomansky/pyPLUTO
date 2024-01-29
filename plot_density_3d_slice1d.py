from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_3d_slice1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R',fontsize=18)
    ax.set_ylabel(r'n',fontsize=18)
    ax.minorticks_on()
    ax.set_yscale('log')
    #plt.axis([0.0,1.0,0.0,1.0])
    
    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0] / 2)
    ypoint = math.floor(D.rho.T.shape[1] / 2)
    V = D.rho.T[zpoint,ypoint,:]*unit_density

    minRho = 0
    maxRho = V[0]
    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length*(xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0]) + xmin*unit_length
    minRho = np.amin(V)
    maxRho = np.amax(V)
    im2 = plt.plot(x, V)  # plotting fluid data.
    plt.savefig('density_3d_slice1d.png')
