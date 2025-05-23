import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray import getScalarArray


def plot_Bturb_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'Bturb.gif', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams['axes.linewidth'] = 0.1
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[8,6])

    D = pp.pload(ntot, varNames=['Bturb'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bturb.shape))

    minBturb = 0
    maxBturb = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Bturb = getScalarArray(D.Bturb, UNIT_VELOCITY*np.sqrt(4*np.pi*UNIT_DENSITY), excl_axis, point)

    minBturb = np.amin(Bturb)
    maxBturb = np.amax(Bturb)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['Bturb'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Bturb = getScalarArray(D.Bturb, UNIT_VELOCITY*np.sqrt(4*np.pi*UNIT_DENSITY), excl_axis, point)
        if(np.amin(Bturb) < minBturb):
            minBturb = np.amin(Bturb)
        if(np.amax(Bturb) > maxBturb):
            maxBturb = np.amax(Bturb)


    print("maxBturb = ", maxBturb)
    print("minBturb = ", minBturb)

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
        f1.set_figheight(8)
        f1.set_figwidth(6)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['Bturb'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Bturb = getScalarArray(D.Bturb, UNIT_VELOCITY*np.sqrt(4*np.pi*UNIT_DENSITY), excl_axis, point)

        np.flip(Bturb, 0)

        im2 = ax.imshow(Bturb, origin='upper', norm=colors.Normalize(vmin=minBturb, vmax=maxBturb), aspect = aspect,
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        if(transponse):
            #np.flip(Bturb, 0)
            im2 = ax.imshow(Bturb.T, origin='lower', norm=colors.Normalize(vmin=minBturb, vmax=maxBturb), aspect=aspect,
                            extent=[ymin, ymax, xmin, xmax])  # plotting fluid data.
        #cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        #cax2 = f1.add_axes()
        #plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        plt.colorbar(im2, orientation='horizontal')  # vertical colorbar for fluid data.
        ax.set_xlabel(r'x, cm', fontsize=14, fontweight='bold')
        ax.set_ylabel(r'y, cm', fontsize=14, fontweight='bold')
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

    f = out_dir + file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
