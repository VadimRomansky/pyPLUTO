from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_profile_3d_slice1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R',fontsize=18)
    ax.set_ylabel(r'Vx',fontsize=18)
    ax.set_yscale('log')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    
    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.vx1.T.shape[0] / 2)
    ypoint = math.floor(D.vx1.T.shape[1] / 2)
    V = np.abs(D.vx1.T[zpoint,ypoint,:])
    P = D.prs.T[zpoint, ypoint, :]
    rho = D.rho.T[zpoint, ypoint, :]

    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length*(xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0]) + xmin*unit_length
    minRho = np.amin(V)
    maxRho = np.amax(V)
    im2 = plt.plot(x,V,'r-',x,P,'g-',x,rho,'b-') # plotting fluid data.
    ax.legend(['vx', 'pressure', 'density'])
    plt.savefig('profile_3d_slice1d.png')
