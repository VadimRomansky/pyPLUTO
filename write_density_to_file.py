import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def write_density_to_file(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, xmin = None, xmax = None, ymin = None, ymax = None, zmin = None, zmax = None):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['rho'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))

    nx = D.rho.shape[0]
    ny = 1
    if(ndim > 1):
        ny = D.rho.shape[1]
    nz = 1
    if(ndim > 2):
        nz = D.rho.shzpe[2]
    Rho = D.rho*UNIT_DENSITY

    outFile = open('density.dat','w')

    npx = nx
    x1 = D.x1r[0]
    x2 = D.x1r[-1]
    if((xmin != None) and (xmax != None)):
        npx = xmax - xmin
        x1 = D.x1r[xmin]
        x2 = D.x1r[xmax]

    npy = ny
    y1 = D.x2r[0]
    y2 = D.x2r[-1]
    if ((ymin != None) and (ymax != None)):
        npy = ymax - ymin
        y1 = D.x2r[ymin]
        y2 = D.x2r[ymax]

    npz = nz
    z1 = D.x3r[0]
    z2 = D.x3r[-1]
    if ((zmin != None) and (zmax != None)):
        npz = zmax - zmin
        z1 = D.x3r[zmin]
        z2 = D.x3r[zmax]

    print(npx, npy, npz, sep = ' ', file = outFile)
    print(x1, y1, z1, sep=' ', file=outFile)
    print(x2, y2, z2, sep=' ', file=outFile)

    for i in range(nx):
        if(((xmin == None) or (xmax == None)) or ((i >= xmin) and (i < xmax))):
            for j in range(ny):
                if (((ymin == None) or (ymax == None)) or ((j >= ymin) and (j < ymax))):
                    for k in range(nz):
                        if (((zmin == None) or (zmax == None)) or ((k >= zmin) and (k < zmax))):
                            if(ndim == 1):
                                print(Rho[i],file=outFile)
                            elif(ndim == 2):
                                print(Rho[i][j], file = outFile)
                            elif(ndim == 3):
                                print(Rho[i][j][k], file = outFile)

    outFile.close()