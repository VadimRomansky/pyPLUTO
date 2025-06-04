import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def plot_pressure(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'pressure.png', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.prs.shape))

    minPrs = 0
    maxPrs = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Prs = getScalarArray(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, excl_axis, point)

    minPrs = np.amin(Prs)
    maxPrs = np.amax(Prs)



    im2 = ax.imshow(Prs, origin='upper', norm = colors.LogNorm(vmin = minPrs, vmax = maxPrs), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    if(transponse):
        #np.flip(Prs, 0)
        im2 = ax.imshow(Prs.T, origin='lower', norm = colors.LogNorm(vmin = minPrs, vmax = maxPrs), aspect=aspect,extent=[D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH, D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'z cm', fontsize=20)
    ax.set_ylabel(r'r cm', fontsize=20)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name, bbox_inches='tight')
    plt.close()