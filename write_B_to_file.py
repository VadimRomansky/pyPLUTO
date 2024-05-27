import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def write_B_to_file(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, xmin = None, xmax = None, ymin = None, ymax = None, zmin = None, zmax = None):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    nx = D.Bx1.shape[0]
    ny = 1
    if(ndim > 1):
        ny = D.Bx1.shape[1]
    nz = 1
    if(ndim > 2):
        nz = D.Bx1.shzpe[2]

    UNIT_FIELD = np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)

    Bx = D.Bx1*UNIT_FIELD
    By = D.Bx2*UNIT_FIELD
    Bz = D.Bx3*UNIT_FIELD

    outFile = open('B.dat','w')

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
                                print(Bx[i], By[i], Bz[i], sep = ' ',file=outFile)
                            elif(ndim == 2):
                                print(Bx[i][j], By[i][j], Bz[i][j], sep = ' ', file = outFile)
                            elif(ndim == 3):
                                print(Bx[i][j][k], By[i][j][k], Bz[i][j][k], sep = ' ', file = outFile)

    outFile.close()