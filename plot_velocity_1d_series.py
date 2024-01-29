from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['text.usetex'] = True

    D = pp.pload(number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    ndim = len((D.vx1.shape))

    minV = 0
    maxV = 0

    nx = D.vx1.shape[0]
    V1 = np.zeros([nx])
    V2 = np.zeros([nx])
    V3 = np.zeros([nx])

    if (ndim == 1):
        Vz = D.vx3[:] * UNIT_VELOCITY / c
        Vy = D.vx2[:] * UNIT_VELOCITY / c
        Vx = D.vx1[:] * UNIT_VELOCITY / c
        V3 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(int(number / 2), varNames=['vx1','vx2','vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:] * UNIT_VELOCITY / c
        Vy = D.vx2[:] * UNIT_VELOCITY / c
        Vx = D.vx1[:] * UNIT_VELOCITY / c
        V2 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(1, varNames=['vx1','vx2','vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:] * UNIT_VELOCITY / c
        Vy = D.vx2[:] * UNIT_VELOCITY / c
        Vx = D.vx1[:] * UNIT_VELOCITY / c
        V1 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        Vz = D.vx3[:, ypoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint] * UNIT_VELOCITY / c
        V3 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(int(number / 2), varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:, ypoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint] * UNIT_VELOCITY / c
        V2 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(1, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:, ypoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint] * UNIT_VELOCITY / c
        V1 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 3):
        ypoint = math.floor(D.vx1.shape[1] / 2)
        zpoint = math.floor(D.vx1.shape[2] / 2)
        Vz = D.vx3[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint, zpoint] * UNIT_VELOCITY / c
        V3 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(int(number / 2), varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint, zpoint] * UNIT_VELOCITY / c
        V2 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        D = pp.pload(1, varNames=['vx1', 'vx2', 'vx3'], w_dir=w_dir, datatype='dbl')
        Vz = D.vx3[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vy = D.vx2[:, ypoint, zpoint] * UNIT_VELOCITY / c
        Vx = D.vx1[:, ypoint, zpoint] * UNIT_VELOCITY / c
        V1 = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))


    minV = min(np.amin(V1), np.amin(V2), np.amin(V3))
    maxV = max(np.amax(V1), np.amax(V2), np.amax(V3))

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / V1.shape[0]
    x = dx * range(V1.shape[0]) + xmin
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$B~G$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, V1,'b', linewidth = 4)
    plt.plot(x, V2,'g', linewidth = 4)
    plt.plot(x, V3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig('velocity_1d_series.png')
