from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_B_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    # f1 = plt.figure(figsize=[10,8])
    f1 = plt.figure()

    D = pp.pload(ntot, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0

    nx = D.Bx1.shape[0]
    B = np.zeros([nx])

    if (ndim == 1):
        Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 2):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 3):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        zpoint = math.floor(D.Bx1.shape[2] / 2)
        Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

    minB = np.amin(B)
    maxB = np.amax(B)

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / B.shape[0]
    x = dx * range(B.shape[0]) + xmin
    startOffset = 2

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype='dbl')
        if (ndim == 1):
            Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 2):
            ypoint = math.floor(D.Bx1.shape[1] / 2)
            Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 3):
            ypoint = math.floor(D.Bx1.shape[1] / 2)
            zpoint = math.floor(D.Bx1.shape[2] / 2)
            Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (np.amin(B) < minB):
            minB = np.amin(B)
        if (np.amax(B) > maxB):
            maxB = np.amax(B)

    def update(frame_number):
        # f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([0.9*minB, 1.1*maxB])
        D = pp.pload(frame_number, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype='dbl')
        if (ndim == 1):
            Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 2):
            ypoint = math.floor(D.Bx1.shape[1] / 2)
            Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        if (ndim == 3):
            ypoint = math.floor(D.Bx1.shape[1] / 2)
            zpoint = math.floor(D.Bx1.shape[2] / 2)
            Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
            B = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))

        ax.set_xlabel(r'x', fontsize=18)
        ax.set_ylabel(r'B', fontsize=18)
        ax.minorticks_on()

        im2 = plt.plot(x, B)  # plotting fluid data.
        # time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1 - startOffset)

    # plt.show()

    f = r"B_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
