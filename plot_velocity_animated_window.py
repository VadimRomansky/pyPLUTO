import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray import getVectorArray


def plot_velocity_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, file_name = 'velocity_window.gif', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    c = 2.998E10
    f1 = plt.figure(figsize=[8,6])
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams['axes.linewidth'] = 0.1

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

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

    if(excl_axis == 3):
        xmin1 = D.x1.min() * UNIT_LENGTH
        xmax1 = D.x1.max() * UNIT_LENGTH
        ymin1 = D.x2.min() * UNIT_LENGTH
        ymax1 = D.x2.max() * UNIT_LENGTH
    elif(excl_axis == 2):
        xmin1 = D.x1.min() * UNIT_LENGTH
        xmax1 = D.x1.max() * UNIT_LENGTH
        ymin1 = D.x3.min() * UNIT_LENGTH
        ymax1 = D.x3.max() * UNIT_LENGTH
    elif(excl_axis == 1):
        xmin1 = D.x2.min() * UNIT_LENGTH
        xmax1 = D.x2.max() * UNIT_LENGTH
        ymin1 = D.x3.min() * UNIT_LENGTH
        ymax1 = D.x3.max() * UNIT_LENGTH
    else:
        print("wrong exclude axis\n")
        return


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        V = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)

        im2 = ax.imshow(V, origin='upper', norm=colors.Normalize(vmin=minV, vmax=maxV), aspect = aspect,
                        extent=[xmin1, xmax1, ymin1, ymax1])  # plotting fluid data.
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        if(transponse):
            #np.flip(V, 0)
            im2 = ax.imshow(V.T, origin='lower', norm=colors.Normalize(vmin=minV, vmax=maxV), aspect=aspect,
                            extent=[ymin1, ymax1, xmin1, xmax1])  # plotting fluid data.
            ax.set_xlim([ymin, ymax])
            ax.set_ylim([xmin, xmax])
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