import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def plot_density_window(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, file_name = 'density_window.png', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1
    ax = f1.add_subplot(111)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    if(transponse):
        ax.set_xlim([ymin, ymax])
        ax.set_ylim([xmin, xmax])

    D = pp.pload(ns, varNames = ['rho'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))

    minRho = 0
    maxRho = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)



    im2 = ax.imshow(Rho, origin='upper', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    if(transponse):
        #np.flip(Rho, 0)
        im2 = ax.imshow(Rho.T, origin='lower', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect=aspect,extent=[D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH, D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'x, cm', fontsize=20, fontweight='bold')
    ax.set_ylabel(r'y, cm', fontsize=20, fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name, bbox_inches='tight')
    plt.close()