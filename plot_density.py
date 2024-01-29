import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_density(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['rho'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))

    minRho = 0
    maxRho = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.rho.shape[0]
    ny = D.rho.shape[1]
    Rho = np.zeros([ny,nx])

    if(ndim == 2):
        Rho = D.rho.T[:, :] * UNIT_DENSITY
    if(ndim == 3):
        zpoint = math.floor(D.rho.T.shape[0] / 2)
        Rho = D.rho.T[zpoint, :, :] * UNIT_DENSITY
    np.flip(Rho,0)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)



    im2 = ax.imshow(Rho, origin='upper', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('density.png')
    plt.close()