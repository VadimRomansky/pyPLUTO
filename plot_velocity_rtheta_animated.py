import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_velocity_rtheta_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'velocity_rtheta.gif'):
    f1 = plt.figure(figsize=[6,8])
    plt.rcParams["figure.dpi"] = 500

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        ny = 10
    else:
        ny = D.vx1.shape[1]

    nx = D.vx1.shape[0]
    V = np.zeros([ny, nx])

    if (ndim == 1):
        Vz = D.vx3.T[:]
        Vy = D.vx2.T[:]
        Vx = D.vx1.T[:]
        for i in range(ny):
            V[i] = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        Vz = D.vx3.T[:, :]
        Vy = D.vx2.T[:, :]
        Vx = D.vx1.T[:, :]
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        zpoint = math.floor(D.vx1.T.shape[0] / 2)
        Vz = D.vx3.T[zpoint, :, :]
        Vy = D.vx2.T[zpoint, :, :]
        Vx = D.vx1.T[zpoint, :, :]
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    np.flip(V, 0)

    minV = np.amin(V)
    maxV = np.amax(V)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            Vz = D.vx3.T[:]
            Vy = D.vx2.T[:]
            Vx = D.vx1.T[:]
            for i in range(ny):
                V[i] = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 2):
            Vz = D.vx3.T[:, :]
            Vy = D.vx2.T[:, :]
            Vx = D.vx1.T[:, :]
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            zpoint = math.floor(D.vx1.T.shape[0] / 2)
            Vz = D.vx3.T[zpoint, :, :]
            Vy = D.vx2.T[zpoint, :, :]
            Vx = D.vx1.T[zpoint, :, :]
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if(np.amin(V) < minV):
            minV = np.amin(V)
        if(np.amax(V) > maxV):
            maxV = np.amax(V)


    print("maxV = ", maxV)
    print("minV = ", minV)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    ymin = D.x2.min() * UNIT_LENGTH
    ymax = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(6)

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            Vz = D.vx3.T[:]
            Vy = D.vx2.T[:]
            Vx = D.vx1.T[:]
            for i in range(ny):
                V[i] = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 2):
            Vz = D.vx3.T[:, :]
            Vy = D.vx2.T[:, :]
            Vx = D.vx1.T[:, :]
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            zpoint = math.floor(D.vx1.T.shape[0] / 2)
            Vz = D.vx3.T[zpoint, :, :]
            Vy = D.vx2.T[zpoint, :, :]
            Vx = D.vx1.T[zpoint, :, :]
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))

        np.flip(V, 0)

        Nfraction = 1
        rad = np.linspace(0, xmax/Nfraction, int(nx/Nfraction))
        azm = np.linspace(D.x2.min() - np.pi/2, D.x2.max() - np.pi/2, ny)
        r, th = np.meshgrid(rad, azm)

        ax = plt.subplot(projection="polar")
        ax.axis("off")

        ax.set_thetamin(D.x2.min() * 180 / np.pi - 90)
        ax.set_thetamax(D.x2.max() * 180 / np.pi - 90)
        V2=V[:,range(int(nx/Nfraction))]
        im2 = plt.pcolormesh(th, r, V2, norm=colors.LogNorm(vmin=minV, vmax=maxV))

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