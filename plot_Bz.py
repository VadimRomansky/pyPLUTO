import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def plot_Bz(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'Bz.png', excl_axis = 3, point = 0.5, aspect = 'equal'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx3.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Bz = getScalarArray(D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)

    minB = np.amin(Bz)
    maxB = np.amax(Bz)



    im2 = ax.imshow(Bz, origin='upper', norm = colors.Normalize(vmin = minB, vmax = maxB), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()