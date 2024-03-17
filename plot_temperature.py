import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_temperature(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 3):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    if(ndim == 2):
        nx = D.T.shape[0]
        ny = D.T.shape[1]
    elif(ndim == 3):
        if(excl_axis == 3):
            nx = D.T.shape[0]
            ny = D.T.shape[1]
        elif(excl_axis == 2):
            nx = D.T.shape[0]
            ny = D.T.shape[2]
        elif(excl_axis == 1):
            nx = D.T.shape[1]
            ny = D.T.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return
    T = np.zeros([ny,nx])

    if(ndim == 2):
        T = D.T.T[:, :]
    if(ndim == 3):
        if(excl_axis == 3):
            zpoint = math.floor(D.T.T.shape[0] *point)
            T = D.T.T[zpoint, :, :] * UNIT_DENSITY
        elif(excl_axis == 2):
            zpoint = math.floor(D.T.T.shape[1] *point)
            T = D.T.T[:, zpoint, :] * UNIT_DENSITY
        elif(excl_axis == 1):
            zpoint = math.floor(D.T.T.shape[2] *point)
            T = D.T.T[:,:,zpoint] * UNIT_DENSITY
        else:
            print("wrong excluded axis\n")
            return
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
    plt.savefig('temperature.png')
    plt.close()