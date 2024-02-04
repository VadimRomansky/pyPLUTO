import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_velocity_y(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    c=2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['vx2'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx2.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.vx2.shape[0]
    ny = D.vx2.shape[1]
    Vy = np.zeros([ny,nx])

    if(ndim == 2):
        Vy = D.vx2.T[:, :]*UNIT_VELOCITY/c
    if(ndim == 3):
        zpoint = math.floor(D.vx2.T.shape[0] / 2)
        Vy = D.vx2.T[zpoint, :, :]*UNIT_VELOCITY/c
    np.flip(Vy,0)

    minV = np.amin(Vy)
    maxV = np.amax(Vy)



    im2 = ax.imshow(Vy, origin='upper', norm = colors.Normalize(vmin = minV, vmax = maxV), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('velcity_y.png')
    plt.close()