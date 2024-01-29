import numpy as np
#from PIL import Image
from pylab import *
from matplotlib import animation
import matplotlib.colors as colors
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_B_animated_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax):
    f1 = plt.figure(figsize=[8,12])
    #f1 = plt.figure()


    #ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
    zpoint = math.floor(D.Bx1.T.shape[0] / 2)
    Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    #Bz = D.Bx3.T[zpoint, :, :]
    By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    #By = D.Bx2.T[zpoint, :, :]
    Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    #Bx = D.Bx1.T[zpoint, :, :]

    # B = D.Bx1.T**2 + D.Bx2.T**2 + D.Bx3.T**2
    nx = shape(D.Bx1.T)[0]
    ny = shape(D.Bx1.T)[1]

    B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

    minB = np.amin(B)
    maxB = np.amax(B)
    print("B[0][0] = ", B[0][0])
    print("B[10][10] = ", B[10][10])


    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #Bx = D.Bx1.T[zpoint, :, :]
        By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #By = D.Bx2.T[zpoint, :, :]
        Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #Bz = D.Bx3.T[zpoint, :, :]
        B = np.sqrt(Bx ** 2 + By ** 2 + Bz ** 2)
        if(np.amin(B) < minB):
            minB = np.amin(B)
        if(np.amax(B) > maxB):
            maxB = np.amax(B)


    print("maxB = ", maxB)
    print("minB = ", minB)

    xmin1 = D.x1.min() * UNIT_LENGTH
    xmax1 = D.x1.max() * UNIT_LENGTH
    ymin1 = D.x2.min() * UNIT_LENGTH
    ymax1 = D.x2.max() * UNIT_LENGTH


    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        f1.set_figheight(8)
        f1.set_figwidth(12)
        ax = f1.add_subplot(111)
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        D = pp.pload(frame_number, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        zpoint = math.floor(D.Bx1.T.shape[0] / 2)
        Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #Bz = D.Bx3.T[zpoint, :, :]
        By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #By = D.Bx2.T[zpoint, :, :]
        Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        #Bx = D.Bx1.T[zpoint, :, :]

        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

        im2 = ax.imshow(B, origin='upper', norm=colors.LogNorm(vmin=minB, vmax=maxB), aspect = 'auto',
                        extent=[xmin1, xmax1, ymin1, ymax1])  # plotting fluid data.
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

    f = r"B_3d_to_2d_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)