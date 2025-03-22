import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray import getScalarArray


def plot_entropy_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, file_name = 'entropy_window.gif', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[8,6])
    plt.rcParams['axes.linewidth'] = 0.1
    plt.rcParams["figure.dpi"] = 200
    gam = 5.0/3.0

    D = pp.pload(ntot, varNames=['rho','prs'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))

    minS = 0
    maxS = 0
    nx = 0
    ny = 0

    if (ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
    Prs = getScalarArray(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, excl_axis, point)

    nx = Rho.shape[0]
    ny = Rho.shape[1]

    S = np.zeros([nx, ny])

    for i in range(nx):
        for j in range(ny):
            S[i][j] = Prs[i][j] / pow(Rho[i][j], gam)

    minS = np.amin(S)
    maxS = np.amax(S)


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['rho','prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
        Prs = getScalarArray(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, excl_axis, point)

        nx = Rho.shape[0]
        ny = Rho.shape[1]

        S = np.zeros([nx, ny])

        for i in range(nx):
            for j in range(ny):
                S[i][j] = Prs[i][j] / pow(Rho[i][j], gam)
        if(np.amin(S) < minS):
            minS = np.amin(S)
        if(np.amax(S) > maxS):
            maxS = np.amax(S)


    print("maxS = ", maxS)
    print("minS = ", minS)

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

        D = pp.pload(frame_number, varNames = ['rho','prs'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
        Rho = getScalarArray(D.rho, UNIT_DENSITY, excl_axis, point)
        Prs = getScalarArray(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, excl_axis, point)

        nx = Rho.shape[0]
        ny = Rho.shape[1]

        S = np.zeros([nx, ny])

        for i in range(nx):
            for j in range(ny):
                S[i][j] = Prs[i][j] / pow(Rho[i][j], gam)

        im2 = ax.imshow(S, origin='upper', norm=colors.LogNorm(vmin=minS, vmax=maxS), aspect = aspect,
                        extent=[xmin1, xmax1, ymin1, ymax1])  # plotting fluid data.
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        if(transponse):
            #np.flip(Rho, 0)
            im2 = ax.imshow(S.T, origin='lower', norm=colors.LogNorm(vmin=minS, vmax=maxS), aspect=aspect,
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