from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_temperature_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True

    D = pp.pload(number, varNames = ['T'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    ndim = len((D.T.shape))

    minT = 0
    maxT = 0

    nx = D.T.shape[0]
    T1 = np.zeros([nx])
    T2 = np.zeros([nx])
    T3 = np.zeros([nx])

    if (ndim == 1):
        T3 = D.T[:]
        D = pp.pload(int(number / 2), varNames=['T'], w_dir=w_dir, datatype=datatype)
        T2 = D.T[:]
        D = pp.pload(1, varNames=['T'], w_dir=w_dir, datatype=datatype)
        T1 = D.T[:]
    if (ndim == 2):
        ypoint = math.floor(D.T.shape[1] / 2)
        T3 = D.T[:, ypoint]
        D = pp.pload(int(number / 2), varNames=['T'], w_dir=w_dir, datatype=datatype)
        T2 = D.T[:, ypoint]
        D = pp.pload(1, varNames=['T'], w_dir=w_dir, datatype=datatype)
        T1 = D.T[:, ypoint]
    if (ndim == 3):
        ypoint = math.floor(D.T.shape[1] / 2)
        zpoint = math.floor(D.T.shape[2] / 2)
        T3 = D.T[:,ypoint, zpoint]
        D = pp.pload(int(number / 2), varNames=['T'], w_dir=w_dir, datatype=datatype)
        T2 = D.T[:, ypoint, zpoint]
        D = pp.pload(1, varNames=['T'], w_dir=w_dir, datatype=datatype)
        T1 = D.T[:, ypoint, zpoint]


    minT = min(np.amin(T1), np.amin(T2), np.amin(T3))
    maxT = max(np.amax(T1), np.amax(T2), np.amax(T3))

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / T1.shape[0]
    x = dx * range(T1.shape[0]) + xmin
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$T$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, T1,'b', linewidth = 4)
    plt.plot(x, T2,'g', linewidth = 4)
    plt.plot(x, T3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig('temperature_1d_series.png')
