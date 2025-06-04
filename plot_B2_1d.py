from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_B2_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'B2_1d.png', axis = 1, out_dir = ""):
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    Bx = D.Bx1*np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    By = D.Bx2*np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    Bz = D.Bx3*np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)

    tBx2 = np.square(Bx)
    tBy2 = np.square(By)
    tBz2 = np.square(Bz)

    Nx = 1

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        Nx = Bx.shape[0]
        dx = (xmax - xmin) / Bx.shape[0]
        x = dx * range(Bx.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        Nx = Bx.shape[1]
        dx = (xmax - xmin) / Bx.shape[1]
        x = dx * range(Bx.shape[1]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        Nx = Bx.shape[2]
        dx = (xmax - xmin) / Bx.shape[2]
        x = dx * range(Bx.shape[2]) + xmin
    else:
        print("wrong axis")
        return

    Bx2 = np.zeros([Nx])
    By2 = np.zeros([Nx])
    Bz2 = np.zeros([Nx])

    if(axis == 1):
        if(len(Bx.shape) == 1):
            Bx2 = tBx2
            By2 = tBy2
            Bz2 = tBz2
        elif (len(Bx.shape) == 2):
            Bx2 = np.sum(tBx2, 1)
            By2 = np.sum(tBy2, 1)
            Bz2 = np.sum(tBz2, 1)
        else :
            Bx2 = np.sum(tBx2, (1,2))
            By2 = np.sum(tBy2, (1,2))
            Bz2 = np.sum(tBz2, (1,2))
    elif(axis == 2):
        Bx2 = np.sum(tBx2, (0,2))
        By2 = np.sum(tBy2, (0,2))
        Bz2 = np.sum(tBz2, (0,2))
    elif(axis == 3):
        Bx2 = np.sum(tBx2, (0,1))
        By2 = np.sum(tBy2, (0,1))
        Bz2 = np.sum(tBz2, (0,1))
    else:
        print("wrong axis")
        return

    minB = np.min([np.amin(Bx2), np.amin(By2), np.amin(Bz2)])
    maxB = np.max([np.amax(Bx2), np.amax(By2), np.amax(Bz2)])

    ax.set_ylabel(r'B^2',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, Bx2, 'r', label = 'Bx^2')
    plt.plot(x, By2, 'g', label = 'By^2')
    plt.plot(x, Bz2, 'b', label = 'Bz^2')

    ax.legend()

    #plt.show()
    plt.savefig(out_dir + file_name)
    plt.close()
