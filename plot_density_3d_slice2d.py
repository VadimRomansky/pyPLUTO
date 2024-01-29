from matplotlib import animation
import matplotlib.colors as colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_3d_slice2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VLOCITY):
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    cax2 = f1.add_axes([0.125, 0.92, 0.775, 0.03])

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0]/2)
    print(zpoint)
    V=D.rho.T[zpoint,:,:]

    
    xmin = D.x1.min()*UNIT_LENGTH
    xmax= D.x1.max()*UNIT_LENGTH
    ymin = D.x2.min()*UNIT_LENGTH
    ymax = D.x2.max()*UNIT_LENGTH
    print(xmin, xmax, ymin, ymax)
    
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    
    minRho = np.amin(V)
    maxRho = np.amax(V)

    im2 = ax.imshow(V, origin='lower', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect = 'auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    #minRho = 0;
    #maxRho = 300;
    im2.set_clim(minRho, maxRho)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    #plt.show()
    plt.savefig('density_3d_to_2d.png')
