from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_1d_series(number, w_dir, unit_density, unit_length, unit_velocity):
    #plt.rcParams['text.usetex'] = True

    D = pp.pload(number, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V3=D.rho.T
    D = pp.pload(int(number/2), varNames=['rho'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
    V2 = D.rho.T
    D = pp.pload(1, varNames=['rho'], w_dir=w_dir, datatype='dbl')  # Load fluid data.
    V1 = D.rho.T
    minRho = min(np.amin(V1), np.amin(V2), np.amin(V3))
    maxRho = max(np.amax(V1), np.amax(V2), np.amax(V3))

    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length * (xmax - xmin) / V1.shape[0]
    x = dx * range(V1.shape[0]) + xmin
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    plt.rcParams['axes.linewidth'] = 4
    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$n~cm^{-3}$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    ax.set_xlim([1E15,1E17])
    ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V1,'b', linewidth = 4)
    plt.plot(x, V2,'g', linewidth = 4)
    plt.plot(x, V3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig('snr.png')
