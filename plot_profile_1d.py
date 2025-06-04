from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_profile_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'profile_1d.png', axis = 1, point1 = 0.5, point2 = 0.5, out_dir = ""):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": 'Times New Roman'
    })
    f1, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex='col')
    f1.set_figheight(8)
    f1.set_figwidth(10)
    plt.subplots_adjust(hspace=.0)

    D = pp.pload(ntot, varNames = ['rho','prs','vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.

    Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
    V = getVectorArray_1d(D.vx1, D.vx2, D.vx3, UNIT_VELOCITY / c, axis, point1, point2)

    nx = Rho.shape[0]

    gam = 5.0 / 3.0

    S = np.zeros([nx])
    for i in range(nx):
        S[i] = Prs[i]/pow(Rho[i], gam)

    S0 = S[int(0.4*nx)]

    S = S/S0

    minRho = np.amin(Rho)
    maxRho = np.amax(Rho)

    minV = np.amin(V)
    maxV = np.amax(V)

    minS = np.amin(S)
    maxS = np.amax(S)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho.shape[0]
        x = dx * range(Rho.shape[0]) + xmin
    else:
        print("wrong axis")
        return


    ax1.set_ylabel(r'$\rho$ [g/cm]$^3$', fontsize=20)
    ax1.set_yscale('log')
    ax2.set_ylabel(r'$v/c$', fontsize=20)
    ax3.set_ylabel(r'S/S$_0$')
    ax3.set_yscale('log')

    ax1.set_xlabel(r'z [pc]', fontsize=20)
    ax2.set_xlabel(r'z [pc]', fontsize=20)
    ax3.set_xlabel(r'z [pc]', fontsize=20)

    ax1.minorticks_on()
    ax2.minorticks_on()
    ax3.minorticks_on()

    #plt.axis([0.0,1.0,0.0,1.0])
    ax1.plot(x, Rho, linewidth = 2)
    ax2.plot(x, V, linewidth=2)
    ax3.plot(x, S, linewidth=2)

    #plt.show()
    plt.savefig(out_dir + file_name, bbox_inches = 'tight')
    plt.close()
