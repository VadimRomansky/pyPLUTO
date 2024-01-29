from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_animated_3d_slice1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure()
    
    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0] / 2)
    ypoint = math.floor(D.rho.T.shape[1] / 2)
    V = D.rho.T[zpoint,ypoint,:]*unit_density

    minRho = 0
    maxRho = V[0]
    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length*(xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0])
    startOffset = 10;

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i+startOffset, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = D.rho.T[zpoint,ypoint,:]*unit_density
        if (np.amin(V) < minRho):
            minRho = np.amin(V)
        if (np.amax(V) > maxRho):
            maxRho = np.amax(V)


    

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_ylim([minRho, maxRho])
        D = pp.pload(frame_number+startOffset, w_dir, datatype='dbl')  # Load fluid data.
        V = D.rho.T[zpoint,ypoint,:]*unit_density
        ax.set_xlabel(r'R', fontsize=18)
        ax.set_ylabel(r'rho', fontsize=18)
        ax.minorticks_on()
        im2 = plt.plot(x,V)  # plotting fluid data.
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1 - startOffset)

    #plt.show()

    f = r"density_3d_to_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
