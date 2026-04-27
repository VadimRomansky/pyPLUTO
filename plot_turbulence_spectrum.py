import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
import sklearn.linear_model
def plot_turbulence_spectrum(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'turbulence_spectrum.png', out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)
    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR', filename='turbulence') # Loading particle data : particles.00ns_ch00.flt

    Nmomentum = len(P.kturb[0])
    F = np.zeros([Nmomentum])
    p = P.kturb[0]
    V = 0

    for i in range(len(P.id)):
        for j in range(Nmomentum):
            F[j] = F[j] + P.W[i][j]*P.dV[i]
            V = V + P.dV[i]

    #for j in range(Nmomentum):
        #if(F[j] <= 0):
            #F[j] = 1E-100
    #for i in range(len(y)):
        #y = y/PVmag[i]
    maxF = np.amax(F)

    startPower = 10
    endPower = 40
    Fp = np.log(F[startPower:endPower])
    pp = np.log(p[startPower:endPower])[:,None]
    #reg = sklearn.linear_model.LinearRegression().fit(pp, Fp)
    #reg.score(pp, Fp)
    #Fp1 = np.exp(reg.predict(pp))
    pp1 = np.exp(pp)

    #labelp = 'p^{' + str(reg.coef_[0])+ '}'

    Fa = np.zeros([Nmomentum])

    Fa[0] = F[0];

    for i in range(Nmomentum):
        #Fa[i] = F[0]
        Fa[i] = F[0]*(p[0]/p[i])**(5.0/3.0)

    plt.plot(p, F, label = 'numerical')
    plt.plot(p, Fa, label = 'k^{-5/3}')
    #plt.plot(pp1, Fp1, label = labelp)
    plt.xscale('log')
    plt.yscale('log')

    #ax.set_ylim([maxF/1E5, 2*maxF])
    ax.legend()

    plt.savefig(out_dir + file_name)
    plt.close()