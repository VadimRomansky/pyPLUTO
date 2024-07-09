import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.

def plot_velocity_rtheta(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'velocity_rtheta.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])

    D = pp.pload(ns, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    nx = D.vx1.shape[0]

    if (ndim == 1):
        ny = 10
    else :
        ny = D.vx1.shape[1]

    V = np.zeros([ny, nx])
    
    if (ndim == 1):
        Vz = D.vx3.T[:]
        Vy = D.vx2.T[:]
        Vx = D.vx1.T[:]
        for i in range(ny):
            V[i] = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        Vz = D.vx3.T[:, :]
        Vy = D.vx2.T[:, :]
        Vx = D.vx1.T[:, :]
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        zpoint = math.floor(D.vx1.T.shape[0] / 2)
        Vz = D.vx3.T[zpoint, :, :]
        Vy = D.vx2.T[zpoint, :, :]
        Vx = D.vx1.T[zpoint, :, :]
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))

    minV = 0.9*amin(V)
    maxV = 1.1*amax(V)

    Nfraction = 1
    rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
    azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
    r, th = np.meshgrid(rad, azm)

    ax = plt.subplot(projection="polar")
    ax.axis("off")

    ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
    ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)

    V1 = V[:,range(int(nx/Nfraction))]
    im2 = plt.pcolormesh(th, r, V1, norm = colors.Normalize(vmin = minV, vmax = maxV))
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minV, maxV)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()
