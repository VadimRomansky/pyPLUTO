import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray
from getVectorArray import getVectorArray


def plot_velocity_quiver(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 0.5):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[50,40])
    ax = f1.add_subplot(111)

    Nsampling = 5

    D = pp.pload(ns, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    V1 = np.zeros([1,1])
    V2 = np.zeros([1,1])
    U = np.zeros([1])
    V = np.zeros([1])
    if(excl_axis == 1):
        V1 = getScalarArray(D.vx2, UNIT_VELOCITY/c, excl_axis, point)
        V2 = getScalarArray(D.vx3, UNIT_VELOCITY/c, excl_axis, point)
        U = D.x2*UNIT_LENGTH
        V = D.x3*UNIT_LENGTH
    elif(excl_axis == 2):
        V1 = getScalarArray(D.vx1, UNIT_VELOCITY/c, excl_axis, point)
        V2 = getScalarArray(D.vx3, UNIT_VELOCITY/c, excl_axis, point)
        U = D.x1*UNIT_LENGTH
        V = D.x3*UNIT_LENGTH
    elif(excl_axis == 3):
        V1 = getScalarArray(D.vx1, UNIT_VELOCITY/c, excl_axis, point)
        V2 = getScalarArray(D.vx2, UNIT_VELOCITY/c, excl_axis, point)
        U = D.x1*UNIT_LENGTH
        V = D.x2*UNIT_LENGTH

    Vel = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c,
                       excl_axis, point)

    V11 = V1[::Nsampling, ::Nsampling]
    V22 = V2[::Nsampling, ::Nsampling]
    Vv = Vel[::Nsampling, ::Nsampling]

    minB = np.amin(Vv)
    maxB = np.amax(Vv)

    #U1, V1 = np.meshgrid(V, U)

    im2 = ax.quiver(U[::Nsampling], V[::Nsampling], V11, V22, Vv, width = 0.001) # plotting fluid data.
    #im2 = ax.quiver(U[::Nsampling], V[::Nsampling], B11, B22, Bb) # plotting fluid data.
    #cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    #plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('velocity_quiver.png')
    plt.close()