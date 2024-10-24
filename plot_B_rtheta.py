import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.

def plot_B_rtheta(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'B_rtheta.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    nx = D.Bx1.shape[0]

    if (ndim == 1):
        ny = 10
    else :
        ny = D.Bx1.shape[1]

    B = np.zeros([ny, nx])
    
    if (ndim == 1):
        Bz = D.Bx3.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        for i in range(ny):
            B[i] = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 2):
        Bz = D.Bx3.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 3):
        zpoint = math.floor(D.Bx1.T.shape[0] / 2)
        Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

    minB = 0.9*amin(B)
    maxB = 1.1*amax(B)

    Nfraction = 1
    rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
    azm = np.linspace(-np.pi/2, np.pi/2, ny)
    r, th = np.meshgrid(rad, azm)

    ax = plt.subplot(projection="polar")
    ax.axis("off")

    ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
    ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)

    B1 = B[:,range(int(nx/Nfraction))]
    im2 = plt.pcolormesh(th, r, B1, norm = colors.Normalize(vmin = minB, vmax = maxB))
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()
