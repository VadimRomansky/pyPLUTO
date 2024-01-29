from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_animated_1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    #f1 = plt.figure(figsize=[10,8])
    f1 = plt.figure()
    #ax = f1.add_subplot(111)

    #ax.set_xlabel(r'R',fontsize=18)
    #ax.set_ylabel(r'n',fontsize=18)
    #ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    
    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V=D.rho.T*unit_density
    minRho = 0
    maxRho = V[0]
    xmin = D.x1.min()*unit_length
    xmax = D.x1.max()*unit_length
    dx = (xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0])
    startOffset = 20;

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i+startOffset, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = D.rho.T*unit_density
        if (np.amin(V) < minRho):
            minRho = np.amin(V)
        if (np.amax(V) > maxRho):
            maxRho = np.amax(V)

    

    def update(frame_number):
        #f1 = plt.figure(figsize=[6, 6])
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_ylim([minRho, maxRho])
        D = pp.pload(frame_number+startOffset, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V=D.rho.T*unit_density

        ax.set_xlabel(r'R', fontsize=18)
        ax.set_ylabel(r'rho',fontsize=18)
        ax.minorticks_on()
      
        im2 = plt.plot(x,V)  # plotting fluid data.
        #time.sleep(1)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1 - startOffset)

    #plt.show()

    f = r"density_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
