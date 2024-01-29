from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_profile_3d_slice1d_window(ntot, w_dir, unit_density, unit_length, unit_velocity, xmin, xmax):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    ax.set_xlabel(r'R',fontsize=18)
    ax.set_ylabel(r'Vx',fontsize=18)
    ax.set_yscale('log')
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    
    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.vx1.T.shape[0] / 2)
    ypoint = math.floor(D.vx1.T.shape[1] / 2)
    V = np.abs(D.vx1.T[zpoint, ypoint, :])
    P = D.prs.T[zpoint, ypoint, :]
    rho = D.rho.T[zpoint, ypoint, :]

    xmin1 = D.x1.min()
    xmax1 = D.x1.max()
    dx = unit_length*(xmax1-xmin1)/V.shape[0]
    x= dx*range(V.shape[0]) + xmin1*unit_length
    
    N1 = 0
    N2 = V.shape[0]

    for i in range(V.shape[0]):
        if(x[i] > xmin):
            N1 = i
            break

    for i in range(V.shape[0]):
        if(x[i] > xmax):
            N2 = i
            break

    x1 = x[N1:N2]
    V1 = V[N1:N2]
    P1 = P[N1:N2]
    rho1 = rho[N1:N2]

    im2 = plt.plot(x1,V1,'r-',x1,P1,'g-',x1,rho1,'b-')  # plotting fluid data.
    ax.legend(['vx', 'pressure','density'])
    plt.savefig('profile_3d_slice1d_window.png')
