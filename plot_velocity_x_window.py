import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_velocity_x_window(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, excl_axis = 3, point = 0.5):
    c=2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    D = pp.pload(ns, varNames = ['vx1'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    if(ndim == 2):
        nx = D.vx1.shape[0]
        ny = D.vx1.shape[1]
    elif(ndim == 3):
        if(excl_axis == 3):
            nx = D.vx1.shape[0]
            ny = D.vx1.shape[1]
        elif(excl_axis == 2):
            nx = D.vx1.shape[0]
            ny = D.vx1.shape[2]
        elif(excl_axis == 1):
            nx = D.vx1.shape[1]
            ny = D.vx1.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return
    Vx = np.zeros([ny,nx])

    if(ndim == 2):
        Vx = D.vx1.T[:, :]*UNIT_VELOCITY/c
    if(ndim == 3):
        if(excl_axis == 3):
            zpoint = math.floor(D.vx1.T.shape[0]* point)
            Vx = D.vx1.T[zpoint, :, :] * UNIT_VELOCITY / c
        elif(excl_axis == 2):
            zpoint = math.floor(D.vx1.T.shape[1]* point)
            Vx = D.vx1.T[:,zpoint, :] * UNIT_VELOCITY / c
        elif(excl_axis == 1):
            zpoint = math.floor(D.vx1.T.shape[2]* point)
            Vx = D.vx1.T[:,:,zpoint] * UNIT_VELOCITY / c
        else:
            print("wrong excluded axis\n")
            return
    np.flip(Vx,0)

    minV = np.amin(Vx)
    maxV = np.amax(Vx)



    im2 = ax.imshow(Vx, origin='upper', norm = colors.Normalize(vmin = minV, vmax = maxV), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('velcity_x_window.png')
    plt.close()