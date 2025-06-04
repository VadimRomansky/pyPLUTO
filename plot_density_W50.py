import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def plot_density_W50(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'density.png', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    f1 = plt.figure(figsize=[10,3])
    plt.rcParams.update({'font.size': 15})
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": 'Times New Roman'
    })
    ax = f1.add_subplot(111)

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

    V1 = Rho[:, 1:int(Rho.shape[1] / 2)]



    im2 = ax.imshow(V1, origin='upper', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, 0.5*D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    if(transponse):
        #np.flip(V, 0)
        im2 = ax.imshow(V1.T, origin='lower', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect=aspect,extent=[D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH, D.x1.min()*UNIT_LENGTH, 0.5*D.x1.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.92,0.17,0.02,0.65])

    cbar = plt.colorbar(im2, cax=cax2, orientation='vertical')  # vertical colorbar for fluid data.
    # cbar = plt.colorbar(im2, orientation='vertical')
    cbar.set_label(r'$\rho$ [g/cm$^3$]', rotation=270)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.tick_params(labelsize=10)

    ax.set_xlabel(r'z [pc]', fontsize=20)
    ax.set_ylabel(r'r [pc]', fontsize=20)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name, bbox_inches='tight')
    plt.close()