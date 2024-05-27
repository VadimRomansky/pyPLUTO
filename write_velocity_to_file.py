import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def write_velocity_to_file(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, xmin = None, xmax = None, ymin = None, ymax = None, zmin = None, zmax = None):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    nx = D.vx1.shape[0]
    ny = 1
    if(ndim > 1):
        ny = D.vx1.shape[1]
    nz = 1
    if(ndim > 2):
        nz = D.vx1.shzpe[2]

    Vx = D.vx1*UNIT_VELOCITY
    Vy = D.vx2*UNIT_VELOCITY
    Vz = D.vx3*UNIT_VELOCITY

    outFile = open('velocity.dat','w')

    npx = nx
    if ((xmin != None) and (xmax != None)):
        npx = xmax - xmin

    npy = ny
    if ((ymin != None) and (ymax != None)):
        npy = ymax - ymin

    npz = nz
    if ((zmin != None) and (zmax != None)):
        npz = zmax - zmin

    print(npx, npy, npz, sep=' ', file=outFile)

    for i in range(nx):
        if (((xmin == None) or (xmax == None)) or ((i >= xmin) and (i < xmax))):
            for j in range(ny):
                if (((ymin == None) or (ymax == None)) or ((j >= ymin) and (j < ymax))):
                    for k in range(nz):
                        if (((zmin == None) or (zmax == None)) or ((k >= zmin) and (k < zmax))):
                            if(ndim == 1):
                                print(Vx[i], Vy[i], Vz[i], sep = ' ',file=outFile)
                            elif(ndim == 2):
                                print(Vx[i][j], Vy[i][j], Vz[i][j], sep = ' ', file = outFile)
                            elif(ndim == 3):
                                print(Vx[i][j][k], Vy[i][j][k], Vz[i][j][k], sep = ' ', file = outFile)

    outFile.close()