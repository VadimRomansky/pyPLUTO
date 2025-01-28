import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_distribution(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'distribution.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)
    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude
    maxU = 1.0
    minU = 1.0
    if (len(PVmag) > 0):
        maxU = max(PVmag)
        minU = min(PVmag)

    logP = np.log10(PVmag)
    #y, x = np.histogram(logP, 50, range=(np.log10(minU), np.log10(maxU + 1)), density=False)
    y, x = np.histogram(PVmag, 200, range=(minU, maxU + 1), density=False)

    x = x[0:len(x) - 1]
    #for i in range(len(y)):
        #y = y/PVmag[i]

    plt.plot(x, y)
    plt.xscale('log')
    plt.yscale('log')

    plt.savefig(file_name)
    plt.close()