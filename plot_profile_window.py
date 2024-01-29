from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_profile_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, datatype):
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R', fontsize=18)
    ax.set_ylabel(r'Vx', fontsize=18)
    ax.set_yscale('log')
    ax.minorticks_on()
    # plt.axis([0.0,1.0,0.0,1.0])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0

    nx = D.vx1.shape[0]
    V = np.zeros([nx])
    P = np.zeros([nx])
    rho = np.zeros([nx])

    if (ndim == 1):
        V = np.abs(D.vx1[:])
        P = D.prs[:]
        rho = D.rho[:]
    if (ndim == 2):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        V = np.abs(D.vx1[:, ypoint])
        P = D.prs[:, ypoint]
        rho = D.rho[:, ypoint]
    if (ndim == 3):
        zpoint = math.floor(D.vx1.T.shape[0] / 2)
        ypoint = math.floor(D.vx1.T.shape[1] / 2)
        V = np.abs(D.vx1[:, ypoint, zpoint])
        P = D.prs[:, ypoint, zpoint]
        rho = D.rho[:, ypoint, zpoint]

    xmin1 = D.x1.min() * UNIT_LENGTH
    xmax1 = D.x1.max() * UNIT_LENGTH
    dx = (xmax1 - xmin1) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin1

    N1 = 0
    N2 = V.shape[0]

    for i in range(V.shape[0]):
        if (x[i] > xmin):
            N1 = i
            break

    for i in range(V.shape[0]):
        if (x[i] > xmax):
            N2 = i
            break

    x1 = x[N1:N2]
    V1 = V[N1:N2]
    P1 = P[N1:N2]
    rho1 = rho[N1:N2]

    im2 = plt.plot(x1, V1, 'r-', x1, P1, 'g-', x1, rho1, 'b-')  # plotting fluid data.
    ax.legend(['vx', 'pressure', 'density'])
    plt.savefig('profile_window.png')
