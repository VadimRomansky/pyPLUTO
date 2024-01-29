from matplotlib import animation, colors
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_B_3d_slice2d_window(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax):
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)

    cax2 = f1.add_axes([0.125, 0.92, 0.775, 0.03])

    D = pp.pload(number, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
    zpoint = math.floor(D.Bx1.T.shape[0] / 2)
    Bz = D.Bx3.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    By = D.Bx2.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    Bx = D.Bx1.T[zpoint, :, :] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)

    # B = D.Bx1.T**2 + D.Bx2.T**2 + D.Bx3.T**2
    nx = shape(D.Bx1.T)[0]
    ny = shape(D.Bx1.T)[1]

    B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    minB = np.amin(B)
    maxB = np.amax(B)
    maxB = 10
    minB = 0.0000001

    im2 = ax.imshow(B, origin='lower', norm=colors.LogNorm(vmin=minB, vmax=maxB), aspect='auto', extent=[D.x1.min() * UNIT_LENGTH, D.x1.max() * UNIT_LENGTH,
                    D.x2.min() * UNIT_LENGTH, D.x2.max() * UNIT_LENGTH])  # plotting fluid data.
    #im2.set_clim(minB, maxB)
    plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
    ax.set_xlabel(r'X', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'Y', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])

    # plt.show()
    plt.savefig('B_3d_slice2d_window.png')
