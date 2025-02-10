import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray
from getVectorArray import getVectorArray


def plot_B_quiver(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'B_quiver.png', excl_axis = 3, point = 0.5, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    Nsampling = 5

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    B1 = np.zeros([1,1])
    B2 = np.zeros([1,1])
    U = np.zeros([1])
    V = np.zeros([1])
    if(excl_axis == 1):
        B1 = getScalarArray(D.Bx2, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        B2 = getScalarArray(D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        U = D.x2*UNIT_LENGTH
        V = D.x3*UNIT_LENGTH
    elif(excl_axis == 2):
        B1 = getScalarArray(D.Bx1, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        B2 = getScalarArray(D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        U = D.x1*UNIT_LENGTH
        V = D.x3*UNIT_LENGTH
    elif(excl_axis == 3):
        B1 = getScalarArray(D.Bx1, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        B2 = getScalarArray(D.Bx2, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)
        U = D.x1*UNIT_LENGTH
        V = D.x2*UNIT_LENGTH

    B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY),
                       excl_axis, point)

    B11 = B1[::Nsampling, ::Nsampling]
    B22 = B2[::Nsampling, ::Nsampling]
    Bb = B[::Nsampling, ::Nsampling]

    minB = np.amin(Bb)
    maxB = np.amax(Bb)

    #U1, V1 = np.meshgrid(V, U)

    im2 = ax.quiver(U[::Nsampling], V[::Nsampling], B11, B22, Bb, width = 0.001) # plotting fluid data.
    #im2 = ax.quiver(U[::Nsampling], V[::Nsampling], B11, B22, Bb) # plotting fluid data.
    #cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    #plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name)
    plt.close()