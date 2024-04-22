import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_B_rtheta_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    f1 = plt.figure(figsize=[6,8])

    D = pp.pload(ntot, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        ny = 10
    else:
        ny = D.Bx1.shape[1]

    nx = D.Bx1.shape[0]
    B = np.zeros([ny, nx])

    if (ndim == 1):
        Bz = D.Bx3.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        for i in range(ny):
            B[i] = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 2):
        Bz = D.Bx3.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 3):
        zpoint = math.floor(D.Bx1.T.shape[0] / 2)
        Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    np.flip(B, 0)

    minB = np.amin(B)
    maxB = np.amax(B)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            Bz = D.Bx3.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            for i in range(ny):
                B[i] = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 2):
            Bz = D.Bx3.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 3):
            zpoint = math.floor(D.Bx1.T.shape[0] / 2)
            Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if(np.amin(B) < minB):
            minB = np.amin(B)
        if(np.amax(B) > maxB):
            maxB = np.amax(B)


    print("maxB = ", maxB)
    print("minB = ", minB)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    ymin = D.x2.min() * UNIT_LENGTH
    ymax = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)

        D = pp.pload(frame_number, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            Bz = D.Bx3.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            for i in range(ny):
                B[i] = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 2):
            Bz = D.Bx3.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 3):
            zpoint = math.floor(D.Bx1.shape[2] / 2)
            Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

        np.flip(B, 0)

        Nfraction = 1
        rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
        azm = np.linspace(-np.pi / 2, np.pi / 2, ny)
        r, th = np.meshgrid(rad, azm)

        ax = plt.subplot(projection="polar")
        ax.axis("off")

        ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
        ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)
        B2=B[:,range(int(nx/Nfraction))]
        im2 = plt.pcolormesh(th, r, B2, norm=colors.LogNorm(vmin=minB, vmax=maxB))

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

    f = r"B_rtheta.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
