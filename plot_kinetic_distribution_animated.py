import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_kinetic_distribution(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'distribution_kinetic.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)
    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    Nmomentum = len(P.p[0])
    F = np.zeros([Nmomentum])
    p = P.p[0]
    V = 0

    for i in range(len(P.id)):
        for j in range(Nmomentum):
            F[j] = F[j] + P.F[i][j]*P.dV[i]
            V = V + P.dV[i]
    #for i in range(len(y)):
        #y = y/PVmag[i]

    plt.plot(p, F)
    plt.xscale('log')
    #plt.yscale('log')

    plt.savefig(file_name)
    plt.close()