from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d


def plot_reverse_shock_wave(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    c = 2.998E10
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    X=np.zeros([ntot+1])

    D = pp.pload(ntot, varNames=['rho', 'vx1'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))
    nx = D.rho.shape[0]
    Rho = np.zeros([nx])
    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin

    upstreamV = np.zeros([ntot+1])

    for i in range(ntot+1):
        D = pp.pload(i, varNames = ['rho','vx1'], w_dir = w_dir, datatype=datatype) # Load fluid data.

        Rho = getScalarArray_1d(D.rho, UNIT_DENSITY, 1, 0.5, 0.5)
        V = getScalarArray_1d(D.vx1, UNIT_VELOCITY, 1, 0.5, 0.5)

        for j in range(nx-10):
            if(Rho[j+10] > 2*Rho[j]):
                X[i] = x[j+10]
                upstreamV[i] = V[j]
                break

    X[0] = 4*24*3600*c

    t=np.zeros([ntot+1])
    for i in range(ntot+1):
        t[i] = i*0.2*UNIT_LENGTH/UNIT_VELOCITY

    ax.set_xlabel(r'$t$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$X_{sh}$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(t, X, 'r-')
    #plt.plot(t, X, 'b-')

    #plt.show()
    plt.savefig('reverse_shock_x.png')

    f2 = plt.figure(figsize=[10,8])
    V = np.zeros([ntot+1])
    V[0] = 0;
    for i in range(ntot):
        V[i+1] = (X[i+1] - X[i])/(t[i+1] - t[i])
    ax2 = f2.add_subplot(111)
    ax2.set_xlabel(r'$t$', fontsize=40, fontweight='bold')
    ax2.set_ylabel(r'$V_{sh}/c$', fontsize=40,fontweight='bold')
    ax2.minorticks_on()
    plt.plot(t, V/c, 'r-')

    plt.savefig('v_reverse_shock_x.png')

    f3 = plt.figure(figsize=[10, 8])
    V1 = np.zeros([ntot+1])
    for i in range(ntot+1):
        V1[i] = (upstreamV[i] - V[i])/(1 - upstreamV[i]*V[i]/(c*c))

    V1[0] = 0
    V1[1] = 0
    ax2 = f3.add_subplot(111)
    ax2.set_xlabel(r'$t$', fontsize=40, fontweight='bold')
    ax2.set_ylabel(r'$V_{sh}/c$', fontsize=40, fontweight='bold')
    ax2.minorticks_on()
    plt.plot(t, V1/c, 'r-')

    plt.savefig('v1_reverse_shock_x.png')
    plt.close()

