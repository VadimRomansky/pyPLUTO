from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation


def plot_profile_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, datatype):
    f1 = plt.figure(figsize=[10, 8])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0

    nx = D.vx1.shape[0]

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / nx
    x = dx * range(nx) + xmin

    N1 = 0
    N2 = nx

    for i in range(nx):
        if (x[i] > xmin):
            N1 = i
            break

    for i in range(nx):
        if (x[i] > xmax):
            N2 = i
            break

    x1 = x[N1:N2]

    V = np.zeros([N2-N1])
    P = np.zeros([N2-N1])
    rho = np.zeros([N2-N1])

    if (ndim == 1):
        V = np.abs(D.vx1[N1:N2])
        P = D.prs[N1:N2]
        rho = D.rho[N1:N2]
    if (ndim == 2):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        V = np.abs(D.vx1[N1:N2, ypoint])
        P = D.prs[N1:N2, ypoint]
        rho = D.rho[N1:N2, ypoint]
    if (ndim == 3):
        zpoint = math.floor(D.vx1.T.shape[0] / 2)
        ypoint = math.floor(D.vx1.T.shape[1] / 2)
        V = np.abs(D.vx1[N1:N2, ypoint, zpoint])
        P = D.prs[N1:N2, ypoint, zpoint]
        rho = D.rho[N1:N2, ypoint, zpoint]

    minV = min(amin(V), amin(P), amin(rho))
    maxV = max(amax(V), amax(P), amax(rho))

    for i in range(ntot+1):
        D = pp.pload(i, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir,
                     datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            V = np.abs(D.vx1[N1:N2])
            P = D.prs[N1:N2]
            rho = D.rho[N1:N2]
        if (ndim == 2):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            V = np.abs(D.vx1[N1:N2, ypoint])
            P = D.prs[N1:N2, ypoint]
            rho = D.rho[N1:N2, ypoint]
        if (ndim == 3):
            zpoint = math.floor(D.vx1.T.shape[0] / 2)
            ypoint = math.floor(D.vx1.T.shape[1] / 2)
            V = np.abs(D.vx1[N1:N2, ypoint, zpoint])
            P = D.prs[N1:N2, ypoint, zpoint]
            rho = D.rho[N1:N2, ypoint, zpoint]

        locmin = min(amin(V), amin(P), amin(rho))
        locmax = max(amax(V), amax(P), amax(rho))
        if(locmin < minV):
            minV = locmin
        if(locmax > maxV):
            maxV = locmax

    if (minV <= 0):
        minV = maxV * 1E-20

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_yscale("log")
        ax.set_ylim([0.5*minV, 2*maxV])

        D = pp.pload(frame_number, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir,
                     datatype=datatype)  # Load fluid data.
        if (ndim == 1):
            V = np.abs(D.vx1[N1:N2])
            P = D.prs[N1:N2]
            rho = D.rho[N1:N2]
        if (ndim == 2):
            ypoint = math.floor(D.vx1.shape[1] / 2)
            V = np.abs(D.vx1[N1:N2, ypoint])
            P = D.prs[N1:N2, ypoint]
            rho = D.rho[N1:N2, ypoint]
        if (ndim == 3):
            zpoint = math.floor(D.vx1.T.shape[0] / 2)
            ypoint = math.floor(D.vx1.T.shape[1] / 2)
            V = np.abs(D.vx1[N1:N2, ypoint, zpoint])
            P = D.prs[N1:N2, ypoint, zpoint]
            rho = D.rho[N1:N2, ypoint, zpoint]

        im2 = plt.plot(x1, V, 'r-', x1, P, 'g-', x1, rho, 'b-')  # plotting fluid data.
        ax.legend(['vx', 'pressure', 'density'])
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1)

    # plt.show()

    f = r"profile_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
