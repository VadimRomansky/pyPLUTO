import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_pressure(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.prs.shape))

    minPrs = 0
    maxPrs = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.prs.shape[0]
    ny = D.prs.shape[1]
    Prs = np.zeros([ny,nx])

    if(ndim == 2):
        Prs = D.prs.T[:, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if(ndim == 3):
        zpoint = math.floor(D.prs.T.shape[0] / 2)
        Prs = D.prs.T[zpoint, :, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    np.flip(Prs,0)

    minPrs = np.amin(Prs)
    maxPrs = np.amax(Prs)



    im2 = ax.imshow(Prs, origin='upper', norm = colors.LogNorm(vmin = minPrs, vmax = maxPrs), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('pressure.png')
    plt.close()