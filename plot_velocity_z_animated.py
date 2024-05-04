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


def plot_velocity_z_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[8,6])

    D = pp.pload(ntot, varNames=['vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx3.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Vz = getScalarArray(D.vx3, UNIT_VELOCITY/c, excl_axis, point)

    minV = np.amin(Vz)
    maxV = np.amax(Vz)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Vz = getScalarArray(D.vx3, UNIT_VELOCITY/c, excl_axis, point)
        if(np.amin(Vz) < minV):
            minV = np.amin(Vz)
        if(np.amax(Vz) > maxV):
            maxV = np.amax(Vz)


    print("maxV = ", maxV)
    print("minV = ", minV)

    if(excl_axis == 3):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        ymin = D.x2.min() * UNIT_LENGTH
        ymax = D.x2.max() * UNIT_LENGTH
    elif(excl_axis == 2):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        ymin = D.x3.min() * UNIT_LENGTH
        ymax = D.x3.max() * UNIT_LENGTH
    elif(excl_axis == 1):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        ymin = D.x3.min() * UNIT_LENGTH
        ymax = D.x3.max() * UNIT_LENGTH
    else:
        print("wrong exclude axis\n")
        return


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Vz = getScalarArray(D.vx3, UNIT_VELOCITY/c, excl_axis, point)

        im2 = ax.imshow(Vz, origin='upper', norm=colors.Normalize(vmin=minV, vmax=maxV), aspect = 'auto',
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        #cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        #cax2 = f1.add_axes()
        #plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        plt.colorbar(im2, orientation='horizontal')  # vertical colorbar for fluid data.
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

    f = r"velocity_z.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
