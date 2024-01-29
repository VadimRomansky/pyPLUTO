from matplotlib import animation, colors
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_By_3d_slice2d_window(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax):
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)

    cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])

    D = pp.pload(number, varNames = ['Bx2'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
    zpoint = math.floor(D.Bx2.T.shape[0] / 2)
    V = np.abs(D.Bx2.T[zpoint,:,:]*np.sqrt(4*np.pi*UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY))
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    minB = np.amin(V)
    maxB = np.amax(V)

    im2 = ax.imshow(V, origin='lower', norm=colors.LogNorm(vmin=minB, vmax=maxB), aspect='auto', extent=[D.x1.min() * UNIT_LENGTH, D.x1.max() * UNIT_LENGTH,
                    D.x2.min() * UNIT_LENGTH, D.x2.max() * UNIT_LENGTH])  # plotting fluid data.
    im2.set_clim(minB, maxB)
    plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
    ax.set_xlabel(r'X', fontsize=18)
    ax.set_ylabel(r'Y', fontsize=18)
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])

    # plt.show()
    plt.savefig('By_3d_slice2d_window.png')
