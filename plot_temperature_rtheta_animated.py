import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_temperature_rtheta_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'temperature_rtheta.gif'):
    f1 = plt.figure(figsize=[6,8])
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(ntot, varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        ny = 10
    else:
        ny = D.T.shape[1]

    nx = D.T.shape[0]
    T = np.zeros([ny, nx])

    if (ndim == 1):
        T1 = D.T.T[:]
        for i in range(ny):
            T[i] = T1
    if (ndim == 2):
        T = D.T.T[:, :]
    if (ndim == 3):
        zpoint = math.floor(D.T.T.shape[0] / 2)
        T = D.T.T[zpoint, :, :]
    np.flip(T, 0)

    minT = np.amin(T)
    maxT = np.amax(T)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            T1 = D.T.T[:]
            for i in range(ny):
                T[i] = T1
        if (ndim == 2):
            T = D.T.T[:, :]
        if (ndim == 3):
            zpoint = math.floor(D.T.T.shape[0] / 2)
            T = D.T.T[zpoint, :, :]
        if(np.amin(T) < minT):
            minT = np.amin(T)
        if(np.amax(T) > maxT):
            maxT = np.amax(T)


    print("maxT = ", maxT)
    print("minT = ", minT)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    ymin = D.x2.min() * UNIT_LENGTH
    ymax = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)

        D = pp.pload(frame_number, varNames = ['T'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            T1 = D.T.T[:]
            for i in range(ny):
                T[i] = T1
        if (ndim == 2):
            T = D.T.T[:, :]
        if (ndim == 3):
            zpoint = math.floor(D.T.T.shape[0] / 2)
            T = D.T.T[zpoint, :, :]

        np.flip(T, 0)

        Nfraction = 1
        rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
        azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
        r, th = np.meshgrid(rad, azm)

        ax = plt.subplot(projection="polar")
        ax.axis("off")

        ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
        ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)
        T2=T[:,range(int(nx/Nfraction))]
        im2 = plt.pcolormesh(th, r, T2, norm=colors.LogNorm(vmin=minT, vmax=maxT))

        #cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        #cax2 = f1.add_axes()
        #plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        plt.colorbar(im2, orientation='horizontal')  # vertical colorbar for fluid data.
        ax.set_xlabel(r'R-axis', fontsize=14)
        ax.set_ylabel(r'Z-axis', fontsize=14)
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

    f = file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()
