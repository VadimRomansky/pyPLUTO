import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_pressure_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[8,6])

    D = pp.pload(ntot, varNames=['prs'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.prs.shape))

    minPrs = 0
    maxPrs = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.prs.shape[0]
    ny = D.prs.shape[1]
    Prs = np.zeros([ny, nx])

    if (ndim == 2):
        Prs = D.prs.T[:, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 3):
        zpoint = math.floor(D.prs.T.shape[0] / 2)
        Prs = D.prs.T[zpoint, :, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY

    minPrs = np.amin(Prs)
    maxPrs = np.amax(Prs)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            Prs = D.prs.T[:, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        if (ndim == 3):
            zpoint = math.floor(D.prs.T.shape[0] / 2)
            Prs = D.prs.T[zpoint, :, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        if(np.amin(Prs) < minPrs):
            minPrs = np.amin(Prs)
        if(np.amax(Prs) > maxPrs):
            maxPrs = np.amax(Prs)


    print("maxRho = ", maxPrs)
    print("minRho = ", minPrs)

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

        D = pp.pload(frame_number, varNames = ['prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 2):
            Prs = D.prs.T[:, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        if (ndim == 3):
            zpoint = math.floor(D.prs.shape[2] / 2)
            Prs = D.prs.T[zpoint, :, :] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY

        np.flip(Prs, 0)

        im2 = ax.imshow(Prs, origin='upper', norm=colors.LogNorm(vmin=minPrs, vmax=maxPrs), aspect = 'auto',
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

    f = r"pressure_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
