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


def plot_velocity_quiver_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[40,30])
    Nsampling = 5

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    V1 = np.zeros([1, 1])
    V2 = np.zeros([1, 1])
    X = np.zeros([1])
    Y = np.zeros([1])

    if (excl_axis == 1):
        V1 = getScalarArray(D.vx2, UNIT_VELOCITY / c, excl_axis, point)
        V2 = getScalarArray(D.vx3, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x2 * UNIT_LENGTH
        Y = D.x3 * UNIT_LENGTH
    elif (excl_axis == 2):
        V1 = getScalarArray(D.vx1, UNIT_VELOCITY / c, excl_axis, point)
        V2 = getScalarArray(D.vx3, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x1 * UNIT_LENGTH
        Y = D.x3 * UNIT_LENGTH
    elif (excl_axis == 3):
        V1 = getScalarArray(D.vx1, UNIT_VELOCITY / c, excl_axis, point)
        V2 = getScalarArray(D.vx2, UNIT_VELOCITY / c, excl_axis, point)
        X = D.x1 * UNIT_LENGTH
        Y = D.x2 * UNIT_LENGTH

    V = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)

    minV = np.amin(V)
    maxV = np.amax(V)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        V = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)
        if(np.amin(V) < minV):
            minV = np.amin(V)
        if(np.amax(V) > maxV):
            maxV = np.amax(V)


    print("maxV = ", maxV)
    print("minV = ", minV)

    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(40)
        f1.set_figwidth(30)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        V = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)
        if (excl_axis == 1):
            V1 = getScalarArray(D.vx2, UNIT_VELOCITY / c, excl_axis, point)
            V2 = getScalarArray(D.vx3, UNIT_VELOCITY / c, excl_axis, point)
            X = D.x2 * UNIT_LENGTH
            Y = D.x3 * UNIT_LENGTH
        elif (excl_axis == 2):
            V1 = getScalarArray(D.vx1, UNIT_VELOCITY / c, excl_axis, point)
            V2 = getScalarArray(D.vx3, UNIT_VELOCITY / c, excl_axis, point)
            X = D.x1 * UNIT_LENGTH
            Y = D.x3 * UNIT_LENGTH
        elif (excl_axis == 3):
            V1 = getScalarArray(D.vx1, UNIT_VELOCITY / c, excl_axis, point)
            V2 = getScalarArray(D.vx2, UNIT_VELOCITY / c, excl_axis, point)
            X = D.x1 * UNIT_LENGTH
            Y = D.x2 * UNIT_LENGTH

        V11 = V1[::Nsampling,::Nsampling]
        V22 = V2[::Nsampling,::Nsampling]
        Vv = V[::Nsampling, ::Nsampling]

        im2 = ax.quiver(X[::Nsampling], Y[::Nsampling], V11, V22, Vv, width = 0.001)  # plotting fluid data.
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

    f = r"velocity_quiver.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
