import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_particles_energy(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'particles_energy.png', out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    mass = 1.5E-24
    c = 2.998E10

    mc2 = mass*c*c


    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    Nmomentum = len(P.p[0])
    p = P.p[0]

    Ecr = np.zeros([ns+1])

    for k in range(ns+1):
        P = pr.ploadparticles(ns, w_dir, datatype=datatype, ptype='CR')
        for i in range(len(P.id)):
            for j in range(Nmomentum):
                dp = 0
                if(j == 0):
                    dp = p[1] - p[0]
                else :
                    dp = p[j] - p[j-1]

                E = mc2*sqrt(1 + p[j]*p[j])

                Ecr[k] = Ecr + P.F[i][j]*p[j]*p[j]*E*dp*P.dV[i]

    time = np.zeros([ns+1])
    for k in range(ns+1):
        time[k] = k

    plt.plot(time, Ecr)

    plt.savefig(out_dir + file_name)
    plt.close()