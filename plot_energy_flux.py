import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray
from getVectorArray import getVectorArray

def plot_energy_flux_cyl(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, zmin1, zmax1, rmax1, zmin2, zmax2, rmax2, datatype, file_name ='density.png', excl_axis = 3, point = 0.5, aspect ='equal', transponse = False):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    # plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 500
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames=['rho','prs','vx1', 'vx2','vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.

    ndim = len((D.vx1.shape))

    Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point).T
    Vx1 = getScalarArray(D.vx1, UNIT_VELOCITY, excl_axis, point).T
    Vx2 = getScalarArray(D.vx2, UNIT_VELOCITY, excl_axis, point).T
    Vx3 = getScalarArray(D.vx3, UNIT_VELOCITY, excl_axis, point).T

    minzindex1 = 0
    maxzindex1 = D.vx1.shape[1]
    maxrindex1 = D.vx1.shape[0]

    for i in range(D.vx1.shape[1]):
        if(D.x2[i]*UNIT_LENGTH > zmin1):
            minzindex1 = i
            break

    for i in range(D.vx1.shape[1]):
        if(D.x2[i]*UNIT_LENGTH > zmax1):
            maxzindex1 = i
            break

    for i in range(D.vx1.shape[0]):
        if(D.x1[i]*UNIT_LENGTH > rmax1):
            maxrindex1 = i
            break

    minzindex2 = 0
    maxzindex2 = D.vx1.shape[1]
    maxrindex2 = D.vx1.shape[0]

    for i in range(D.vx1.shape[1]):
        if (D.x2[i] * UNIT_LENGTH > zmin2):
            minzindex2 = i
            break

    for i in range(D.vx1.shape[1]):
        if (D.x2[i] * UNIT_LENGTH > zmax2):
            maxzindex2 = i
            break

    for i in range(D.vx1.shape[0]):
        if (D.x1[i] * UNIT_LENGTH > rmax2):
            maxrindex2 = i
            break

    print('maxrindex1 = ', maxrindex1)
    print('minzindex1 = ', minzindex1)
    print('maxzindex1 = ', maxzindex1)

    evaluate_flux_cyl_1(D, Rho, UNIT_LENGTH, Vx1, Vx2, Vx3, c, maxrindex1, maxzindex1, minzindex1)
    evaluate_flux_cyl_1(D, Rho, UNIT_LENGTH, Vx1, Vx2, Vx3, c, maxrindex2, maxzindex2, minzindex2)

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

    Rho = Rho.T


    if (transponse):
        # np.flip(Rho, 0)
        im2 = ax.imshow(Rho.T, origin='lower', norm=colors.LogNorm(vmin=minRho, vmax=maxRho), aspect=aspect,
                        extent=[D.x2.min() * UNIT_LENGTH, D.x2.max() * UNIT_LENGTH, D.x1.min() * UNIT_LENGTH,
                                D.x1.max() * UNIT_LENGTH])  # plotting fluid data.
    else :
        im2 = ax.imshow(Rho, origin='upper', norm=colors.LogNorm(vmin=minRho, vmax=maxRho), aspect=aspect,
                        extent=[D.x1.min() * UNIT_LENGTH, D.x1.max() * UNIT_LENGTH, D.x2.min() * UNIT_LENGTH,
                                D.x2.max() * UNIT_LENGTH])  # plotting fluid data.

    cax2 = f1.add_axes([0.125, 0.92, 0.775, 0.03])

    plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.

    x1 = np.zeros([4])
    y1 = np.zeros([4])

    x1[0] = 0
    x1[1] = rmax1
    x1[2] = rmax1
    x1[3] = 0

    y1[0] = zmin1
    y1[1] = zmin1
    y1[2] = zmax1
    y1[3] = zmax1

    if(transponse):
        x1[0] = zmin1
        x1[1] = zmin1
        x1[2] = zmax1
        x1[3] = zmax1

        y1[0] = 0
        y1[1] = rmax1
        y1[2] = rmax1
        y1[3] = 0

    x2 = np.zeros([4])
    y2 = np.zeros([4])

    x2[0] = 0
    x2[1] = rmax2
    x2[2] = rmax2
    x2[3] = 0

    y2[0] = zmin2
    y2[1] = zmin2
    y2[2] = zmax2
    y2[3] = zmax2

    if (transponse):
        x2[0] = zmin2
        x2[1] = zmin2
        x2[2] = zmax2
        x2[3] = zmax2

        y2[0] = 0
        y2[1] = rmax2
        y2[2] = rmax2
        y2[3] = 0

    ax.plot(x1,y1, 'r', linewidth = 0.5)
    ax.plot(x2,y2, 'green', linewidth = 0.5)

    ax.set_xlabel(r'X-axis', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40, fontweight='bold')
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()


def evaluate_flux_cyl_1(D, Rho, UNIT_LENGTH, Vx1, Vx2, Vx3, c, maxrindex1, maxzindex1, minzindex1):
    fluxtop1 = 0.0
    fluxbottom1 = 0.0
    fluxside1 = 0.0
    for i in range(maxrindex1 + 1):
        V2 = (Vx1[i][maxzindex1] * Vx1[i][maxzindex1] + Vx2[i][maxzindex1] * Vx2[i][maxzindex1] + Vx3[i][maxzindex1] *
              Vx3[i][maxzindex1])
        gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
        fluxtop1 += 2 * np.pi * D.x1[i] * D.dx1[i] * Rho[i][maxzindex1] * Vx2[i][maxzindex1] * (
                    gamma - 1.0) * c * c * UNIT_LENGTH * UNIT_LENGTH

        V2 = (Vx1[i][minzindex1] * Vx1[i][minzindex1] + Vx2[i][minzindex1] * Vx2[i][minzindex1] + Vx3[i][minzindex1] *
              Vx3[i][minzindex1])
        gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
        fluxbottom1 -= 2 * np.pi * D.x1[i] * D.dx1[i] * Rho[i][minzindex1] * Vx2[i][minzindex1] * (
                    gamma - 1.0) * c * c * UNIT_LENGTH * UNIT_LENGTH
    for i in range(minzindex1, maxzindex1):
        V2 = (Vx1[maxrindex1][i] * Vx1[maxrindex1][i] + Vx2[maxrindex1][i] * Vx2[maxrindex1][i] + Vx3[maxrindex1][i] *
              Vx3[maxrindex1][i])
        gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
        fluxside1 += 2 * np.pi * D.x1[maxrindex1] * D.dx2[i] * Rho[maxrindex1][i] * Vx1[maxrindex1][i] * (
                    gamma - 1.0) * c * c * UNIT_LENGTH * UNIT_LENGTH
    totalFlux1 = fluxtop1 + fluxbottom1 + fluxside1
    print('top flux 1 = ', fluxtop1)
    print('bottom flux 1 = ', fluxbottom1)
    print('side flux 1 = ', fluxside1)
    print('total flux 1 = ', totalFlux1)