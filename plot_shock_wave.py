from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_shock_wave(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    X=np.zeros([ntot])

    D = pp.pload(ntot, varNames=['rho'], w_dir=w_dir, datatype=datatype)  # Load fluid data.
    ndim = len((D.rho.shape))
    nx = D.rho.shape[0]
    Rho = np.zeros([nx])
    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax - xmin) / Rho.shape[0]
    x = dx * range(Rho.shape[0]) + xmin

    for i in range(ntot):
        D = pp.pload(i, varNames = ['rho'], w_dir = w_dir, datatype=datatype) # Load fluid data.

        if (ndim == 1):
            Rho = D.rho[:] * UNIT_DENSITY
        if (ndim == 2):
            ypoint = math.floor(D.rho.shape[1] / 2)
            Rho = D.rho[:, ypoint] * UNIT_DENSITY
        if (ndim == 3):
            ypoint = math.floor(D.rho.shape[1] / 2)
            zpoint = math.floor(D.rho.shape[2] / 2)
            Rho = D.rho[:,ypoint, zpoint] * UNIT_DENSITY

        for j in range(nx-10):
            if(Rho[nx-11-j] > 2*Rho[nx-1-j]):
                X[i] = x[nx-11-j];
                break;

    Xapprox = np.zeros([ntot])
    Xapprox[ntot-1] = X[ntot-1]
    for i in range(ntot-1):
        Xapprox[i] = Xapprox[ntot-1]*(i*1.0/(ntot-1))**(4.0/5.0)

    ax.set_xlabel(r'$t$', fontsize=40, fontweight='bold')
    ax.set_ylabel(r'$X_{sh}$', fontsize=40,fontweight='bold')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.plot(range(ntot), X, 'r-')
    plt.plot(range(ntot), Xapprox, 'b-')

    #plt.show()
    plt.savefig('shock_x.png')
