import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.

def plot_pressure_rtheta(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'pressure_rtheta.png', out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1

    D = pp.pload(ns, varNames = ['prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    
    ndim = len((D.prs.shape))

    minPrs = 0
    maxPrs = 0
    nx = 0
    ny = 0

    nx = D.prs.shape[0]

    if (ndim == 1):
        ny = 10
    else :
        ny = D.prs.shape[1]

    prs = np.zeros([ny, nx])
    
    if (ndim == 1):
        prs1 = D.prs.T[:] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        for i in range(ny):
            prs[i] = prs1
    if (ndim == 2):
        prs = D.prs.T[:, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 3):
        zpoint = math.floor(D.prs.T.shape[0] / 2)
        prs = D.prs.T[zpoint, :, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY

    minPrs = 0.9*amin(prs)
    maxPrs = 1.1*amax(prs)

    Nfraction = 1
    rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
    azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
    r, th = np.meshgrid(rad, azm)

    ax = plt.subplot(projection="polar")
    ax.axis("off")

    ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
    ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)

    prs2 = prs[:,range(int(nx/Nfraction))]
    im2 = plt.pcolormesh(th, r, prs2, norm = colors.Normalize(vmin = minPrs, vmax = maxPrs))
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minPrs, maxPrs)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'x, cm', fontsize=20, fontweight='bold')
    ax.set_ylabel(r'y, cm', fontsize=20, fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name)
    plt.close()
