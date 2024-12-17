from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_entropy_1d_series(number, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'entropy_1d_series.png', axis = 1, point1 = 0.5, point2 = 0.5):
    plt.rcParams.update({'font.size': 15})
    f1 = plt.figure(figsize=[12, 10])
    ax = f1.add_subplot(111)
    plt.rcParams["figure.dpi"] = 500
    #plt.rcParams['text.usetex'] = True

    gam = 5.0/3.0

    D = pp.pload(number, varNames = ['rho','prs'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    Rho3 = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs3 = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
    D = pp.pload(int(number/2), varNames=['rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Rho2 = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs2 = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)
    D = pp.pload(0, varNames=['rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    Rho1 = getScalarArray_1d(D.rho, UNIT_DENSITY, axis, point1, point2)
    Prs1 = getScalarArray_1d(D.prs, UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY, axis, point1, point2)

    nx = Rho3.shape[0]

    S1 = np.zeros([nx])
    S2 = np.zeros([nx])
    S3 = np.zeros([nx])

    for i in range(nx):
        S1[i] = Prs1[i]*pow(Rho1[i],gam)
        S2[i] = Prs2[i]*pow(Rho2[i],gam)
        S3[i] = Prs3[i]*pow(Rho3[i],gam)

    minS = min(np.amin(S1), np.amin(S2), np.amin(S3))
    maxS = max(np.amax(S1), np.amax(S2), np.amax(S3))

    if (axis == 1):
        xmin = D.x1.min() * UNIT_LENGTH
        xmax = D.x1.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho1.shape[0]
        x = dx * range(Rho1.shape[0]) + xmin
    elif (axis == 2):
        xmin = D.x2.min() * UNIT_LENGTH
        xmax = D.x2.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho1.shape[0]
        x = dx * range(Rho1.shape[0]) + xmin
    elif (axis == 3):
        xmin = D.x3.min() * UNIT_LENGTH
        xmax = D.x3.max() * UNIT_LENGTH
        dx = (xmax - xmin) / Rho1.shape[0]
        x = dx * range(Rho1.shape[0]) + xmin
    else:
        print("wrong axis")
        return
    

    ax.set_xlabel(r'$r~cm$', fontsize=40,fontweight='bold')
    ax.set_ylabel(r'$S$', fontsize=40,fontweight='bold')
    ax.tick_params(axis='x', size=10, width = 4)
    ax.tick_params(axis='y', size=10, width = 4)
    #ax.set_yscale("log")
    #ax.set_xlim([1E15,1E17])
    #ax.set_xscale("log")
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(x, S1,'b', linewidth = 4)
    plt.plot(x, S2,'g', linewidth = 4)
    plt.plot(x, S3,'r', linewidth = 4)
    ax.legend([r'$t = 10^6$', r'$t = 2\cdot10^7$', r'$t = 4\cdot10^7$'], fontsize="40")

    #plt.show()
    plt.savefig(file_name)
    plt.close()