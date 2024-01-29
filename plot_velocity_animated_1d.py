from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_velocity_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    # f1 = plt.figure(figsize=[10,8])
    c = 2.998E10
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0

    nx = D.vx1.shape[0]
    V = np.zeros([nx])

    if (ndim == 1):
        Vz = D.vx3[:]*UNIT_VELOCITY/c
        Vy = D.vx2[:]*UNIT_VELOCITY/c
        Vx = D.vx1[:]*UNIT_VELOCITY/c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        Vz = D.vx3[:, ypoint]*UNIT_VELOCITY/c
        Vy = D.vx2[:, ypoint]*UNIT_VELOCITY/c
        Vx = D.vx1[:, ypoint]*UNIT_VELOCITY/c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        zpoint = math.floor(D.vx1.shape[2] / 2)
        Vz = D.vx3[:, ypoint, zpoint]*UNIT_VELOCITY/c
        Vy = D.vx2[:, ypoint, zpoint]*UNIT_VELOCITY/c
        Vx = D.vx1[:, ypoint, zpoint]*UNIT_VELOCITY/c
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))

    minV = np.amin(V)
    maxV = np.amax(V)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        if (ndim == 1):
            Vz = D.vx3[:]*UNIT_VELOCITY/c
            Vy = D.vx2[:]*UNIT_VELOCITY/c
            Vx = D.vx1[:]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 2):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            Vz = D.vx3[:, ypoint]*UNIT_VELOCITY/c
            Vy = D.vx2[:, ypoint]*UNIT_VELOCITY/c
            Vx = D.vx1[:, ypoint]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            zpoint = math.floor(D.vx1.shape[2] / 2)
            Vz = D.vx3[:, ypoint, zpoint]*UNIT_VELOCITY/c
            Vy = D.vx2[:, ypoint, zpoint]*UNIT_VELOCITY/c
            Vx = D.vx1[:, ypoint, zpoint]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (np.amin(V) < minV):
            minV = np.amin(V)
        if (np.amax(V) > maxV):
            maxV = np.amax(V)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minV, 1.1*maxV])
        D = pp.pload(frame_number, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        if (ndim == 1):
            Vz = D.vx3[:]*UNIT_VELOCITY/c
            Vy = D.vx2[:]*UNIT_VELOCITY/c
            Vx = D.vx1[:]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 2):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            Vz = D.vx3[:, ypoint]*UNIT_VELOCITY/c
            Vy = D.vx2[:, ypoint]*UNIT_VELOCITY/c
            Vx = D.vx1[:, ypoint]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        if (ndim == 3):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            zpoint = math.floor(D.vx1.shape[2] / 2)
            Vz = D.vx3[:, ypoint, zpoint]*UNIT_VELOCITY/c
            Vy = D.vx2[:, ypoint, zpoint]*UNIT_VELOCITY/c
            Vx = D.vx1[:, ypoint, zpoint]*UNIT_VELOCITY/c
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))

        ax.set_xlabel(r'x', fontsize=18)
        ax.set_ylabel(r'v/c', fontsize=18)
        ax.minorticks_on()

        im2 = plt.plot(x, V)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"velocity_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
