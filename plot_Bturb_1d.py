from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d


def plot_Bturb_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY,datatype, file_name = 'B_turb_1d.png', axis = 1, point1 = 0.5, point2 = 0.5, out_dir = ""):
    f1 = plt.figure(figsize=[10,8])
    plt.rcParams["figure.dpi"] = 500
    ax = f1.add_subplot(111)

    D = pp.pload(ntot, varNames = ['Bturb'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    B = getScalarArray_1d(D.Bturb, np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY), axis, point1, point2)

    minB = np.amin(B)
    maxB = np.amax(B)

    if(axis == 1):
        xmin = D.x1.min()*UNIT_LENGTH
        xmax = D.x1.max()*UNIT_LENGTH
        dx = (xmax - xmin) / B.shape[0]
        x = dx * range(B.shape[0]) + xmin
    elif(axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / B.shape[0]
        x = dx * range(B.shape[0]) + xmin
    elif(axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / B.shape[0]
        x = dx * range(B.shape[0]) + xmin
    else:
        print("wrong axis")
        return

    ax.set_ylabel(r'B',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, B)

    #plt.show()
    plt.savefig(out_dir + file_name)
    plt.close()
