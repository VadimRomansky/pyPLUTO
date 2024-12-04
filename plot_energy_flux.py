import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray
from getVectorArray import getVectorArray

def plot_energy_flux_cyl(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, zmin, zmax, rmax, datatype, file_name = 'density.png', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    # plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10, 8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames=['rho','prs','vx1', 'vx2','vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.

    ndim = len((D.vx1.shape))

    Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point).T
    Vx1 = getScalarArray(D.vx1, UNIT_VELOCITY, excl_axis, point).T
    Vx2 = getScalarArray(D.vx2, UNIT_VELOCITY, excl_axis, point).T
    Vx3 = getScalarArray(D.vx3, UNIT_VELOCITY, excl_axis, point).T

    minzindex = 0
    maxzindex = D.vx1.shape[1]
    maxrindex = D.vx1.shape[0]

    for i in range(D.vx1.shape[1]):
        if(D.x2[i]*UNIT_LENGTH > zmin):
            minzindex = i
            break

    for i in range(D.vx1.shape[1]):
        if(D.x2[i]*UNIT_LENGTH > zmax):
            maxzindex = i
            break

    for i in range(D.vx1.shape[0]):
        if(D.x1[i]*UNIT_LENGTH > rmax):
            maxrindex = i
            break

    print('maxrindex = ', maxrindex)
    print('minzindex = ', minzindex)
    print('maxzindex = ', maxzindex)

    fluxtop = 0.0
    fluxbottom = 0.0
    fluxside = 0.0

    for i in range(maxrindex+1):
        V2 = (Vx1[i][maxzindex]*Vx1[i][maxzindex] + Vx2[i][maxzindex]*Vx2[i][maxzindex] + Vx3[i][maxzindex]*Vx3[i][maxzindex])
        gamma = 1.0/np.sqrt(1.0 - V2/(c*c))
        fluxtop += 2*np.pi*D.x1[i]*D.dx1[i]*Rho[i][maxzindex]*Vx2[i][maxzindex]*(gamma - 1.0)*c*c*UNIT_LENGTH*UNIT_LENGTH

        V2 = (Vx1[i][minzindex]*Vx1[i][minzindex] + Vx2[i][minzindex]*Vx2[i][minzindex] + Vx3[i][minzindex]*Vx3[i][minzindex])
        gamma = 1.0/np.sqrt(1.0 - V2/(c*c))
        fluxbottom -= 2*np.pi*D.x1[i]*D.dx1[i]*Rho[i][minzindex]*Vx2[i][minzindex]*(gamma - 1.0)*c*c*UNIT_LENGTH*UNIT_LENGTH

    for i in range(minzindex,maxzindex):
        V2 = (Vx1[maxrindex][i]*Vx1[maxrindex][i] + Vx2[maxrindex][i]*Vx2[maxrindex][i] + Vx3[maxrindex][i]*Vx3[maxrindex][i])
        gamma = 1.0/np.sqrt(1.0 - V2/(c*c))
        fluxside += 2*np.pi*D.x1[maxrindex]*D.dx2[i]*Rho[maxrindex][i]*Vx1[maxrindex][i]*(gamma - 1.0)*c*c*UNIT_LENGTH*UNIT_LENGTH

    totalFlux = fluxtop + fluxbottom + fluxside

    print('top flux = ', fluxtop)
    print('bottom flux = ', fluxbottom)
    print('side flux = ', fluxside)
    print('total flux = ', totalFlux)