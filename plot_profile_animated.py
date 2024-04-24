from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_profile_animated(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, axis = 1, point1 = 0.5, point2 = 0.5):
    c = 2.998E10
    f1 = plt.figure(figsize=[10, 8])

    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, axis, point1, point2)
    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[1]
        x = dx * range(Rho.shape[1]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[2]
        x = dx * range(Rho.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    minV = min(amin(V), amin(Prs), amin(Rho))
    maxV = max(amax(V), amax(Prs), amax(Rho))

    for i in range(ntot+1):
        D = pp.pload(i, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho'], w_dir=w_dir,
                     datatype=datatype)  # Load fluid data.
        V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, axis, point1, point2)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

        locmin = min(amin(V), amin(Prs), amin(Rho))
        locmax = max(amax(V), amax(Prs), amax(Rho))
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
        V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)
        Prs = getScalarArray_1d(D.prs, UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY, axis, point1, point2)
        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)

        im2 = plt.plot(x, V, 'r-', x, Prs, 'g-', x, Rho, 'b-')  # plotting fluid data.
        ax.legend(['vx', 'pressure', 'density'])
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1)

    # plt.show()

    f = r"profile.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()