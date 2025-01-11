import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray


def write_temperature_to_file(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, xmin = None, xmax = None, ymin = None, ymax = None, zmin = None, zmax = None):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    nx = D.T.shape[0]
    ny = 1
    if(ndim > 1):
        ny = D.T.shape[1]
    nz = 1
    if(ndim > 2):
        nz = D.T.shape[2]
    T = D.T*UNIT_DENSITY

    outFile = open('T.dat','w')

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

    if(D.geometry == 'CARTESIAN'):
        print(x1*UNIT_LENGTH, y1*UNIT_LENGTH, z1*UNIT_LENGTH, sep=' ', file=outFile)
        print(x2*UNIT_LENGTH, y2*UNIT_LENGTH, z2*UNIT_LENGTH, sep=' ', file=outFile)
    elif(D.geometry == 'CYLINDRICAL'):
        print(x1 * UNIT_LENGTH, y1 * UNIT_LENGTH, z1, sep=' ', file=outFile)
        print(x2 * UNIT_LENGTH, y2 * UNIT_LENGTH, z2, sep=' ', file=outFile)
    elif(D.geometry == 'POLAR'):
        print(x1 * UNIT_LENGTH, y1, z1 * UNIT_LENGTH, sep=' ', file=outFile)
        print(x2 * UNIT_LENGTH, y2, z2 * UNIT_LENGTH, sep=' ', file=outFile)
    elif(D.geometry == 'SPHERICAL'):
        print(x1 * UNIT_LENGTH, y1, z1, sep=' ', file=outFile)
        print(x2 * UNIT_LENGTH, y2, z2, sep=' ', file=outFile)
    else :
        print("unknown geometry")

    eV = 1.6E-12
    kBoltzman = 1.38E-12

    for i in range(nx):
        if(((xmin == None) or (xmax == None)) or ((i >= xmin) and (i < xmax))):
            for j in range(ny):
                if (((ymin == None) or (ymax == None)) or ((j >= ymin) and (j < ymax))):
                    for k in range(nz):
                        if (((zmin == None) or (zmax == None)) or ((k >= zmin) and (k < zmax))):
                            if(ndim == 1):
                                print(T[i]/(eV*kBoltzman),file=outFile)
                            elif(ndim == 2):
                                print(T[i][j]/(eV*kBoltzman), file = outFile)
                            elif(ndim == 3):
                                print(T[i][j][k]/(eV*kBoltzman), file = outFile)


    outFile.close()