from matplotlib import animation, colors
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

def plot_B_window(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    nx = D.Bx1.shape[0]
    ny = D.Bx1.shape[1]
    B = np.zeros([nx,ny])

    if(ndim == 2):
        Bz = D.Bx3[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if(ndim == 3):
        zpoint = math.floor(D.Bx1.T.shape[0] / 2)
        Bz = D.Bx3[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    np.flip(B, 0)

    minB = np.amin(B)
    maxB = np.amax(B)



    im2 = ax.imshow(B, origin='upper', norm = colors.LogNorm(vmin = minB, vmax = maxB), aspect='auto',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.775,0.03])
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y-axis', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('B_window.png')
    plt.close()