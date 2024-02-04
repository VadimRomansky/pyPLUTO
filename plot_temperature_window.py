import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_temperature_window(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    D = pp.pload(ns, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.T.shape[0]
    ny = D.T.shape[1]
    T = np.zeros([ny,nx])

    if(ndim == 2):
        T = D.T.T[:, :]
    if(ndim == 3):
        zpoint = math.floor(D.T.T.shape[0] / 2)
        T = D.T.T[zpoint, :, :]
    np.flip(T,0)

    minT = np.amin(T)
    maxT = np.amax(T)



    im2 = ax.imshow(T, origin='upper', norm = colors.LogNorm(vmin = minT, vmax = maxT), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('temperature_window.png')
    plt.close()