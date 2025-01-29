import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray_1d import getScalarArray_1d


def plot_kinetic_distribution_at_p_along_axis(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, ppoint, axis = 1, point1 = 0.5, point2 = 0.5, file_name = 'distribution_kinetic_at_p.png'):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames=['rho', 'vx1'], w_dir=w_dir, datatype=datatype)  # Load fluid data.

    ndim = len((D.rho.shape))
    Nx = D.rho.shape[0]
    Ny = 1
    Nz = 1
    if (ndim == 1):
        if (axis != 1):
            print("wrong axis\n")
            return
    if (ndim == 2):
        Ny = D.rho.shape[1]
    if (ndim == 3):
        Nz = D.rho.shape[2]

    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    Nmomentum = len(P.p[0])
    F = np.zeros([Nx])
    p = P.p[0]
    V = 0

    jj =int(point1*Ny)
    kk = int(point2*Nz)

    for i in range(len(P.id)):
        if((int(P.j[i]) == jj) and (int(P.k[i]) == kk)):
                F[int(P.i[i])-3] = P.F[i][ppoint]

    for j in range(Nx):
        if(F[j] <= 0):
            F[j] = 1E-100
    #for i in range(len(y)):
        #y = y/PVmag[i]

    swpoint = int(0.5*Nx)

    x = D.x1*UNIT_LENGTH
    v = 0
    if(ndim == 1):
        v = D.vx1[0]*UNIT_VELOCITY
    if(ndim == 2):
        v = D.vx1[0][jj]*UNIT_VELOCITY
    if(ndim == 3):
        v = D.vx1[0][jj][kk]*UNIT_VELOCITY

    mp = 1.6E-24
    q = 4.84E-10
    u = p[ppoint]
    B = 1E-5
    c = 2.998E10

    Diff = u*mp*c*c*c/(3.0*q*B)

    Diff = 1E25

    Fa = np.zeros([Nx])

    for i in range(Nx):
        if(i < swpoint):
            Fa[i] = F[swpoint]*exp(v*(D.x1[i] - D.x1[swpoint])*UNIT_LENGTH/Diff)
        else:
            Fa[i] = F[swpoint]


    plt.plot(D.x1*UNIT_LENGTH, F)
    plt.plot(D.x1*UNIT_LENGTH, Fa)
    #plt.xscale('log')
    plt.yscale('log')

    plt.savefig(file_name)
    plt.close()