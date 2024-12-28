import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.

def plot_temperature_rtheta(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'temperature_rtheta.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1

    D = pp.pload(ns, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0
    nx = 0
    ny = 0

    nx = D.T.shape[0]

    if (ndim == 1):
        ny = 10
    else :
        ny = D.T.shape[1]

    T = np.zeros([ny, nx])
    
    if (ndim == 1):
        T1 = D.T.T[:]
        for i in range(ny):
            T[i] = T1
    if (ndim == 2):
        T = D.T.T[:, :]
    if (ndim == 3):
        zpoint = math.floor(D.T.T.shape[0] / 2)
        T = D.T.T[zpoint, :, :]

    minT = 0.9*amin(T)
    maxT = 1.1*amax(T)

    Nfraction = 1
    rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
    azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
    r, th = np.meshgrid(rad, azm)

    ax = plt.subplot(projection="polar")
    ax.axis("off")

    ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
    ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)

    T2 = T[:,range(int(nx/Nfraction))]
    im2 = plt.pcolormesh(th, r, T2, norm = colors.Normalize(vmin = minT, vmax = maxT))
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minT, maxT)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()
