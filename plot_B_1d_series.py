from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_B_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True

    D = pp.pload(number, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    ndim = len((D.Bx1.shape))

    minB = 0
    maxB = 0

    nx = D.Bx1.shape[0]
    B1 = np.zeros([nx])
    B2 = np.zeros([nx])
    B3 = np.zeros([nx])

    if (ndim == 1):
        Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B3 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(int(number / 2), varNames=['Bx1','Bx2','Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B2 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(1, varNames=['Bx1','Bx2','Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B1 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 2):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B3 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(int(number / 2), varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B2 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(1, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B1 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
    if (ndim == 3):
        ypoint = math.floor(D.Bx1.shape[1] / 2)
        zpoint = math.floor(D.Bx1.shape[2] / 2)
        Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B3 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(int(number / 2), varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B2 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))
        D = pp.pload(1, varNames=['Bx1', 'Bx2', 'Bx3'], w_dir=w_dir, datatype=datatype)
        Bz = D.Bx3[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        By = D.Bx2[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        Bx = D.Bx1[:, ypoint, zpoint] * np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
        B1 = np.sqrt(np.square(Bx) + np.square(By) + np.square(Bz))


    minB = min(np.amin(B1), np.amin(B2), np.amin(B3))
    maxB = max(np.amax(B1), np.amax(B2), np.amax(B3))

    xmin = D.x1.min() * UNIT_LENGTH
    xmax = D.x1.max() * UNIT_LENGTH
    dx = (xmax - xmin) / B1.shape[0]
    x = dx * range(B1.shape[0]) + xmin
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
    plt.plot(x, B1,'b', linewidth = 4)
    plt.plot(x, B2,'g', linewidth = 4)
    plt.plot(x, B3,'r', linewidth = 4)
    #ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig('B_1d_series.png')
