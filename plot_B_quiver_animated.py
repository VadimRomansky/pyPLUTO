import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray import getScalarArray
from getVectorArray import getVectorArray


def plot_B_quiver_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[8,6])
    Nsampling = 5

    D = pp.pload(ntot, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    B1 = np.zeros([1, 1])
    B2 = np.zeros([1, 1])
    X = np.zeros([1])
    Y = np.zeros([1])

    if (excl_axis == 1):
        B1 = getScalarArray(D.Bx2, UNIT_VELOCITY / c, excl_axis, point)
        B2 = getScalarArray(D.Bx3, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x2 * UNIT_LENGTH
        Y = D.x3 * UNIT_LENGTH
    elif (excl_axis == 2):
        B1 = getScalarArray(D.Bx1, UNIT_VELOCITY / c, excl_axis, point)
        B2 = getScalarArray(D.Bx3, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x1 * UNIT_LENGTH
        Y = D.x3 * UNIT_LENGTH
    elif (excl_axis == 3):
        B1 = getScalarArray(D.Bx1, UNIT_VELOCITY / c, excl_axis, point)
        B2 = getScalarArray(D.Bx2, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x1 * UNIT_LENGTH
        Y = D.x2 * UNIT_LENGTH

    B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, UNIT_VELOCITY/c, excl_axis, point)

    minB = np.amin(B)
    maxB = np.amax(B)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, UNIT_VELOCITY/c, excl_axis, point)
        if(np.amin(B) < minB):
            minB = np.amin(B)
        if(np.amax(B) > maxB):
            maxB = np.amax(B)


    print("maxB = ", maxB)
    print("minB = ", minB)

    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        B = getVectorArray(D.Bx1, D.Bx2, D.Bx3, UNIT_VELOCITY/c, excl_axis, point)
        if (excl_axis == 1):
            B1 = getScalarArray(D.Bx2, UNIT_VELOCITY / c, excl_axis, point)
            B2 = getScalarArray(D.Bx3, UNIT_VELOCITY / c, excl_axis, point)
        elif (excl_axis == 2):
            B1 = getScalarArray(D.Bx1, UNIT_VELOCITY / c, excl_axis, point)
            B2 = getScalarArray(D.Bx3, UNIT_VELOCITY / c, excl_axis, point)
        elif (excl_axis == 3):
            B1 = getScalarArray(D.Bx1, UNIT_VELOCITY / c, excl_axis, point)
            B2 = getScalarArray(D.Bx2, UNIT_VELOCITY / c, excl_axis, point)

        B11 = B1[::Nsampling,::Nsampling]
        B22 = B2[:Nsampling,::Nsampling]
        Bb = B[::Nsampling, ::Nsampling]

        im2 = ax.quiver(X[::Nsampling], Y[::Nsampling], B11, B22, Bb, width = 0.001)  # plotting fluid data.
        #cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        #cax2 = f1.add_axes()
        #plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        #plt.colorbar(im2, orientation='horizontal')  # vertical colorbar for fluid data.
        ax.set_xlabel(r'X-axis', fontsize=14)
        ax.set_ylabel(r'Y-axis', fontsize=14)
        ax.minorticks_on()
        # plt.axis([0.0,1.0,0.0,1.0])
        #plt.savefig(f'B_3d_slice2d_{frame_number}.png')
        #plt.close()
        return im2

    #img, *imgs = [update(f) for f in range(ntot+1)]
    #img.save(fp="B_3d_to_2d.gif", format='GIF', append_images=imgs,
    #         save_all=True, duration=200, loop=0)

    #for i in range(ntot+1):
    #    update(i)

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1)

    f = r"B_quiver.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
