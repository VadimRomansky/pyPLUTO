import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.

def plot_density_rtheta(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    matplotlib.rcParams['figure.subplot.left'] = 0.01
    matplotlib.rcParams['figure.subplot.bottom'] = 0
    matplotlib.rcParams['figure.subplot.right'] = 0.99
    matplotlib.rcParams['figure.subplot.top'] = 1
    f1 = plt.figure(figsize=[10,4])

    D = pp.pload(ns, varNames = ['rho'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    
    ndim = len((D.rho.shape))

    minRho = 0
    maxRho = 0
    nx = 0
    ny = 0

    nx = D.rho.shape[0]

    if (ndim == 1):
        ny = 10
    else :
        ny = D.rho.shape[1]

    rho = np.zeros([ny, nx])
    
    if (ndim == 1):
        rho1 = D.rho.T[:] * UNIT_DENSITY
        for i in range(ny):
            rho[i] = rho1
    if (ndim == 2):
        rho = D.rho.T[:, :] * UNIT_DENSITY
    if (ndim == 3):
        zpoint = math.floor(D.rho.T.shape[0] / 2)
        rho = D.rho.T[zpoint, :, :] * UNIT_DENSITY

    minRho = 0.9*amin(rho)
    maxRho = 1.1*amax(rho)

    Nfraction = 1
    rad = np.linspace(xmin, xmax/Nfraction, int(nx/Nfraction))
    azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
    print("theta min = ", D.x2.min()-np.pi/2)
    print("theta max = ", D.x2.max()-np.pi/2)
    r, th = np.meshgrid(rad, azm)
            
    ax = plt.subplot(projection="polar")
    #ax = f1.add_subplot(111)
    ax.axis("off")

    ax.set_thetamin(D.x2.min()*180/np.pi - 90)
    ax.set_thetamax(D.x2.max()*180/np.pi - 90)
    rho2 = rho[:,range(int(nx/Nfraction))]
    im2 = plt.pcolormesh(th, r, rho2, norm = colors.LogNorm(vmin = minRho, vmax = maxRho))
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minRho, maxRho)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    #ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    #ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    #ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('density_rtheta.png')
    plt.close()
