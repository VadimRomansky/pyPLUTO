from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_temperature_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['T'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0

    nx = D.T.shape[0]
    T = np.zeros([nx])

    if (ndim == 1):
        T = D.T[:]
    if (ndim == 2):
        ypoint = math.floor(D.T.shape[1] / 2)
        T = D.T[:, ypoint]
    if (ndim == 3):
        ypoint = math.floor(D.T.shape[1] / 2)
        zpoint = math.floor(D.T.shape[2] / 2)
        T = D.T[:, ypoint, zpoint]

    minT = np.amin(T)
    maxT = np.amax(T)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / T.shape[0]
    x = dx * range(T.shape[0]) + xmin
    startOffset = 20

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['T'], w_dir=w_dir, datatype=datatype)
        if (ndim == 1):
            T = D.T[:]
        if (ndim == 2):
            ypoint = math.floor(D.T.shape[1] / 2)
            T = D.T[:, ypoint]
        if (ndim == 3):
            ypoint = math.floor(D.T.shape[1] / 2)
            zpoint = math.floor(D.T.shape[2] / 2)
            T = D.T[:, ypoint, zpoint]
        if (np.amin(T) < minT):
            minT = np.amin(T)
        if (np.amax(T) > maxT):
            maxT = np.amax(T)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minT, 1.1*maxT])
        D = pp.pload(frame_number, varNames=['T'], w_dir=w_dir, datatype=datatype)
        if (ndim == 1):
            T = D.T[:]
        if (ndim == 2):
            ypoint = math.floor(D.T.shape[1] / 2)
            T = D.T[:, ypoint]
        if (ndim == 3):
            ypoint = math.floor(D.T.shape[1] / 2)
            zpoint = math.floor(D.T.shape[2] / 2)
            T = D.T[:, ypoint, zpoint]

        ax.set_xlabel(r'$x~cm$', fontsize=40, fontweight='bold')
        ax.set_ylabel(r'$T$', fontsize=40, fontweight='bold')
        ax.minorticks_on()

        im2 = plt.plot(x, T)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"temperature_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
