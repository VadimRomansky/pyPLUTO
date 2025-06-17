from matplotlib import animation, colors
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getVectorArray import getVectorArray


def plot_B_window_W50(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, datatype, file_name = 'B_window.png', excl_axis = 3, point = 0.5, aspect = 'equal', transponse = False, out_dir = ""):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,3])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": 'Times New Roman'
    })
    ax = f1.add_subplot(111)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
    if(transponse):
        ax.set_xlim([ymin, ymax])
        ax.set_ylim([xmin, xmax])

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minV = 0
    maxV = 0
    nx = 0
    ny = 0

    if(ndim == 1):
        print("cant plot 2d image of 1d setup\n")
        return

    #V = getVectorArray(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY/c, excl_axis, point)
    V = getVectorArray(D.Bx1, D.Bx2, D.Bx3, 1000000*np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), excl_axis, point)

    minV = np.amin(V)
    maxV = np.amax(V)



    im2 = ax.imshow(V, origin='upper', norm = colors.LogNorm(vmin = minV, vmax = maxV), aspect=aspect,extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    if(transponse):
        #np.flip(V, 0)
        im2 = ax.imshow(V.T, origin='lower', norm = colors.LogNorm(vmin = minV, vmax = maxV), aspect=aspect,extent=[D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH, D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.92,0.17,0.02,0.65])

    cbar = plt.colorbar(im2, cax=cax2, orientation='vertical')  # vertical colorbar for fluid data.
    # cbar = plt.colorbar(im2, orientation='vertical')
    cbar.set_label(r'B [$\mu$G]', rotation=270)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.tick_params(labelsize=10)
    ax.set_xlabel(r'z [pc]', fontsize=20)
    ax.set_ylabel(r'r [pc]', fontsize=20)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(out_dir + file_name, bbox_inches='tight')
    plt.close()