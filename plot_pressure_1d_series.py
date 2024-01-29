from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_pressure_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True

    D = pp.pload(number, varNames = ['prs'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    ndim = len((D.prs.shape))

    minRho = 0
    maxRho = 0

    nx = D.prs.shape[0]
    Prs1 = np.zeros([nx])
    Prs2 = np.zeros([nx])
    Prs3 = np.zeros([nx])

    if (ndim == 1):
        Prs3 = D.prs[:] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(int(number / 2), varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs2 = D.prs[:] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(1, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs1 = D.prs[:] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 2):
        ypoint = math.floor(D.prs.shape[1] / 2)
        Prs3 = D.prs[:, ypoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(int(number / 2), varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs2 = D.rho[:, ypoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(1, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs1 = D.rho[:, ypoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
    if (ndim == 3):
        ypoint = math.floor(D.prs.shape[1] / 2)
        zpoint = math.floor(D.prs.shape[2] / 2)
        Prs3 = D.prs[:,ypoint, zpoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(int(number / 2), varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs2 = D.prs[:, ypoint, zpoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY
        D = pp.pload(1, varNames=['prs'], w_dir=w_dir, datatype=datatype)
        Prs1 = D.prs[:, ypoint, zpoint] * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY


    minRho = min(np.amin(Prs1), np.amin(Prs2), np.amin(Prs3))
    maxRho = max(np.amax(Prs1), np.amax(Prs2), np.amax(Prs3))

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / Prs1.shape[0]
    x = dx * range(Prs1.shape[0]) + xmin
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$P~g~cm^{-1}~s^{-2}$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, Prs1,'b', linewidth = 4)
    plt.plot(x, Prs2,'g', linewidth = 4)
    plt.plot(x, Prs3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig('pressure_1d_series.png')
