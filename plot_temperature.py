import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def plot_temperature(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 3, aspect = 'equal'):
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

    T = getScalarArray(D.T, 1.0, excl_axis, point)

    minT = np.amin(T)
    maxT = np.amax(T)



    im2 = ax.imshow(T, origin='upper', norm = colors.LogNorm(vmin = minT, vmax = maxT), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])

    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('temperature.png')
    plt.close()