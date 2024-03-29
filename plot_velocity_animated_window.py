import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_velocity_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, excl_axis = 3, point = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[8,6])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    if(ndim == 2):
        nx = D.vx1.shape[0]
        ny = D.vx1.shape[1]
    elif(ndim == 3):
        if(excl_axis == 3):
            nx = D.vx1.shape[0]
            ny = D.vx1.shape[1]
        elif(excl_axis == 2):
            nx = D.vx1.shape[0]
            ny = D.vx1.shape[2]
        elif(excl_axis == 1):
            nx = D.vx1.shape[1]
            ny = D.vx1.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return
    V = np.zeros([ny, nx])

    if (ndim == 2):
        Vz = D.vx3.T[:, :] * UNIT_VELOCITY / c
        Vy = D.vx2.T[:, :] * UNIT_VELOCITY / c
        Vx = D.vx1.T[:, :] * UNIT_VELOCITY / c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        if(excl_axis == 3):
            zpoint = math.floor(D.vx1.T.shape[0]* point)
            Vz = D.vx3.T[zpoint, :, :] * UNIT_VELOCITY / c
            Vy = D.vx2.T[zpoint, :, :] * UNIT_VELOCITY / c
            Vx = D.vx1.T[zpoint, :, :] * UNIT_VELOCITY / c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(excl_axis == 2):
            zpoint = math.floor(D.vx1.T.shape[1]* point)
            Vz = D.vx3.T[:,zpoint, :] * UNIT_VELOCITY / c
            Vy = D.vx2.T[:,zpoint, :] * UNIT_VELOCITY / c
            Vx = D.vx1.T[:,zpoint, :] * UNIT_VELOCITY / c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(excl_axis == 1):
            zpoint = math.floor(D.vx1.T.shape[2]* point)
            Vz = D.vx3.T[:,:,zpoint] * UNIT_VELOCITY / c
            Vy = D.vx2.T[:,:,zpoint] * UNIT_VELOCITY / c
            Vx = D.vx1.T[:,:,zpoint] * UNIT_VELOCITY / c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        else:
            print("wrong excluded axis\n")
            return
    np.flip(V, 0)

    minV = np.amin(V)
    maxV = np.amax(V)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            Vz = D.vx3.T[:, :] * UNIT_VELOCITY / c
            Vy = D.vx2.T[:, :] * UNIT_VELOCITY / c
            Vx = D.vx1.T[:, :] * UNIT_VELOCITY / c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            if (excl_axis == 3):
                zpoint = math.floor(D.vx1.T.shape[0] * point)
                Vz = D.vx3.T[zpoint, :, :] * UNIT_VELOCITY / c
                Vy = D.vx2.T[zpoint, :, :] * UNIT_VELOCITY / c
                Vx = D.vx1.T[zpoint, :, :] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            elif (excl_axis == 2):
                zpoint = math.floor(D.vx1.T.shape[1] * point)
                Vz = D.vx3.T[:, zpoint, :] * UNIT_VELOCITY / c
                Vy = D.vx2.T[:, zpoint, :] * UNIT_VELOCITY / c
                Vx = D.vx1.T[:, zpoint, :] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            elif (excl_axis == 1):
                zpoint = math.floor(D.vx1.T.shape[2] * point)
                Vz = D.vx3.T[:, :, zpoint] * UNIT_VELOCITY / c
                Vy = D.vx2.T[:, :, zpoint] * UNIT_VELOCITY / c
                Vx = D.vx1.T[:, :, zpoint] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            else:
                print("wrong excluded axis\n")
                return
        if(np.amin(V) < minV):
            minV = np.amin(V)
        if(np.amax(V) > maxV):
            maxV = np.amax(V)


    print("maxV = ", maxV)
    print("minV = ", minV)

    xmin1 = D.x1.min() * UNIT_LENGTH
    xmax1 = D.x1.max() * UNIT_LENGTH
    ymin1 = D.x2.min() * UNIT_LENGTH
    ymax1 = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            Vz = D.vx3.T[:, :] * UNIT_VELOCITY / c
            Vy = D.vx2.T[:, :] * UNIT_VELOCITY / c
            Vx = D.vx1.T[:, :] * UNIT_VELOCITY / c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            if (excl_axis == 3):
                zpoint = math.floor(D.vx1.T.shape[0] * point)
                Vz = D.vx3.T[zpoint, :, :] * UNIT_VELOCITY / c
                Vy = D.vx2.T[zpoint, :, :] * UNIT_VELOCITY / c
                Vx = D.vx1.T[zpoint, :, :] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            elif (excl_axis == 2):
                zpoint = math.floor(D.vx1.T.shape[1] * point)
                Vz = D.vx3.T[:, zpoint, :] * UNIT_VELOCITY / c
                Vy = D.vx2.T[:, zpoint, :] * UNIT_VELOCITY / c
                Vx = D.vx1.T[:, zpoint, :] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            elif (excl_axis == 1):
                zpoint = math.floor(D.vx1.T.shape[2] * point)
                Vz = D.vx3.T[:, :, zpoint] * UNIT_VELOCITY / c
                Vy = D.vx2.T[:, :, zpoint] * UNIT_VELOCITY / c
                Vx = D.vx1.T[:, :, zpoint] * UNIT_VELOCITY / c
                V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
            else:
                print("wrong excluded axis\n")
                return

        np.flip(V, 0)

        im2 = ax.imshow(V, origin='upper', norm=colors.Normalize(vmin=minV, vmax=maxV), aspect = 'auto',
                        extent=[xmin1, xmax1, ymin1, ymax1])  # plotting fluid data.
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
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

    f = r"velocity_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
