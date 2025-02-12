import numpy as np
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def getUgradP(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):

    mass = 1.5E-24
    c = 2.998E10

    mc2 = mass*c*c

    D = pp.pload(ns, varNames=['vx1','vx2','vx3','Pkin'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    ugradP = np.zeros(D.vx1.shape)

    if D.geometry == 'CARTESIAN' :
        if(ndim == 3):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
            Nz = D.vx1.shape[2]
        elif (ndim == 2):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
        else:
            Nx = D.vx1.shape[0]
    elif D.geometry == 'CYLINDRICAL' :
        if(ndim == 3):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
            Nz = D.vx1.shape[2]
        elif (ndim == 2):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]

            for i in range(Nx):
                for j in range(Ny):
                    dV = np.pi*(D.x1r[i+1]*D.x1r[i+1] - D.x1r[i]*D.x1r[i])*(D.x2r[j+1] - D.x2r[j])

                    vx = D.vx1[i][j]
                    vy = D.vx2[i][j]
                    ugradP[i][j] = 0
                    if(vx >=0):
                        if(i > 0):
                            ugradP[i][j] = ugradP[i][j] + dV*vx*(D.Pkin[i][j] - D.Pkin[i-1][j])/(D.x1[i] - D.x1[i-1])
                        else :
                            ugradP[i][j] = ugradP[i][j] + dV*vx*(D.Pkin[i+1][j] - D.Pkin[i][j])/(D.x1[i+1] - D.x1[i])
                    else :
                        if(i < Nx - 1):
                            ugradP[i][j] = ugradP[i][j] + dV*vx*(D.Pkin[i+1][j] - D.Pkin[i][j])/(D.x1[i+1] - D.x1[i])
                        else :
                            ugradP[i][j] = ugradP[i][j] + dV*vx*(D.Pkin[i][j] - D.Pkin[i-1][j])/(D.x1[i] - D.x1[i-1])

                    if(vy >= 0):
                        if(j > 0):
                            ugradP[i][j] = ugradP[i][j] + dV*vy*(D.Pkin[i][j] - D.Pkin[i][j-1])/(D.x1[i]*(D.x2[j] - D.x2[j-1]))
                        else :
                            ugradP[i][j] = ugradP[i][j] + dV*vy*(D.Pkin[i][j+1] - D.Pkin[i][j])/(D.x1[i]*(D.x2[j+1] - D.x2[j]))
                    else :
                        if(j < Ny - 1):
                            ugradP[i][j] = ugradP[i][j] + dV*vy*(D.Pkin[i][j+1] - D.Pkin[i][j])/(D.x1[i]*(D.x2[j+1] - D.x2[j]))
                        else :
                            ugradP[i][j] = ugradP[i][j] + dV*vy*(D.Pkin[i][j] - D.Pkin[i][j-1])/(D.x1[i]*(D.x2[j] - D.x2[j-1]))
        else:
            Nx = D.vx1.shape[0]
    elif D.geometry == 'POLAR' :
        if(ndim == 3):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
            Nz = D.vx1.shape[2]
        elif (ndim == 2):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
        else:
            Nx = D.vx1.shape[0]
    elif D.geometry == 'SPHERICAL':
        if(ndim == 3):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
            Nz = D.vx1.shape[2]
        elif (ndim == 2):
            Nx = D.vx1.shape[0]
            Ny = D.vx1.shape[1]
        else:
            Nx = D.vx1.shape[0]

    return ugradP
