import numpy as np
from matplotlib import colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from getScalarArray import getScalarArray
from getVectorArray import getVectorArray


def plot_B_quiver_window(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, file_name = 'B_quiver_window.png', excl_axis = 3, point = 0.5, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 1000
    ax = f1.add_subplot(111)

    Nsampling = 4

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

    B = B.T
    B1 = B1.T
    B2 = B2.T

    Nx = U.shape[0]
    Ny = V.shape[0]
    minXindex = 0
    for i in range(Nx):
        if(U[i] >= xmin):
            minXindex = i
            break

    maxXindex = Nx-1
    for i in range(Nx):
        if(U[Nx - i - 1] <= xmax):
            maxXindex = Nx - i - 1
            break

    minYindex = 0
    for i in range(Ny):
        if (V[i] >= ymin):
            minYindex = i
            break

    maxYindex = Ny-1
    for i in range(Ny):
        if (V[Ny - i - 1] <= ymax):
            maxYindex = Ny - i - 1
            break

    U1 = U[minXindex:maxXindex]
    V1 = V[minYindex:maxYindex]

    print(minXindex, maxXindex, minYindex, maxYindex)

    B111 = B1[minXindex:maxXindex, minYindex:maxYindex]
    B222 = B2[minXindex:maxXindex, minYindex:maxYindex]
    Bbb = B[minXindex:maxXindex, minYindex:maxYindex]

    B11 = B111[::Nsampling, ::Nsampling]
    B22 = B222[::Nsampling, ::Nsampling]
    Bb = Bbb[::Nsampling, ::Nsampling]

    U11 = U1[::Nsampling]
    V11 = V1[::Nsampling]

    #minB = np.amin(Bb)
    #maxB = np.amax(Bb)

    #U1, V1 = np.meshgrid(V, U)

    ax.set_xlim([ymin, ymax])
    ax.set_ylim([xmin, xmax])

    #im2 = ax.quiver(U11, V11, B11.T, B22.T, Bb.T, width = 0.001) # plotting fluid data.
    im2 = ax.quiver(V11, U11, B22, B11, Bb, width=0.001)  # plotting fluid data.
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