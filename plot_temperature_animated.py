import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_temperature_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, excl_axis = 3, point = 0.5):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[8,12])

    D = pp.pload(ntot, varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    if(ndim == 2):
        nx = D.T.shape[0]
        ny = D.T.shape[1]
    elif(ndim == 3):
        if(excl_axis == 3):
            nx = D.T.shape[0]
            ny = D.T.shape[1]
        elif(excl_axis == 2):
            nx = D.T.shape[0]
            ny = D.T.shape[2]
        elif(excl_axis == 1):
            nx = D.T.shape[1]
            ny = D.T.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return
    T = np.zeros([ny, nx])

    if (ndim == 2):
        T = D.T[:, :]
    if (ndim == 3):
        if(excl_axis == 3):
            zpoint = math.floor(D.T.T.shape[0] *point)
            T = D.T.T[zpoint, :, :] * UNIT_DENSITY
        elif(excl_axis == 2):
            zpoint = math.floor(D.T.T.shape[1] *point)
            T = D.T.T[:, zpoint, :] * UNIT_DENSITY
        elif(excl_axis == 1):
            zpoint = math.floor(D.T.T.shape[2] *point)
            T = D.T.T[:,:,zpoint] * UNIT_DENSITY
        else:
            print("wrong excluded axis\n")
            return

    minT = np.amin(T)
    maxT = np.amax(T)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            T = D.T[:, :]
        if (ndim == 3):
            if (excl_axis == 3):
                zpoint = math.floor(D.T.T.shape[0] * point)
                T = D.T.T[zpoint, :, :] * UNIT_DENSITY
            elif (excl_axis == 2):
                zpoint = math.floor(D.T.T.shape[1] * point)
                T = D.T.T[:, zpoint, :] * UNIT_DENSITY
            elif (excl_axis == 1):
                zpoint = math.floor(D.T.T.shape[2] * point)
                T = D.T.T[:, :, zpoint] * UNIT_DENSITY
            else:
                print("wrong excluded axis\n")
                return
        if(np.amin(T) < minT):
            minT = np.amin(T)
        if(np.amax(T) > maxT):
            maxT = np.amax(T)


    print("maxT = ", maxT)
    print("minT = ", minT)

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
        f1.set_figwidth(12)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            T = D.T[:, :]
        if (ndim == 3):
            if (excl_axis == 3):
                zpoint = math.floor(D.T.T.shape[0] * point)
                T = D.T.T[zpoint, :, :] * UNIT_DENSITY
            elif (excl_axis == 2):
                zpoint = math.floor(D.T.T.shape[1] * point)
                T = D.T.T[:, zpoint, :] * UNIT_DENSITY
            elif (excl_axis == 1):
                zpoint = math.floor(D.T.T.shape[2] * point)
                T = D.T.T[:, :, zpoint] * UNIT_DENSITY
            else:
                print("wrong excluded axis\n")
                return

        np.flip(T, 0)

        im2 = ax.imshow(T, origin='upper', norm=colors.LogNorm(vmin=minT, vmax=maxT), aspect = 'auto',
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

    f = r"temperature.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)