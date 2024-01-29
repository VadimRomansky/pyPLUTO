from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_animated_1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    f1 = plt.figure(figsize=[10,8])

    
    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V = np.sqrt(D.vx1.T ** 2 + D.vx2.T ** 2 + D.vx3.T ** 2)
    minV = 0
    maxV = V[0]
    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    dx = (xmax-xmin)/V.shape[0]
    x= dx*range(V.shape[0])
    startOffset = 20;

    for i in range(ntot - startOffset + 1):
        D = pp.pload(i+startOffset, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = np.sqrt(D.vx1.T ** 2 + D.vx2.T ** 2 + D.vx3.T ** 2)
        if (np.amin(V) < minV):
            minV = np.amin(V)
        if (np.amax(V) > maxV):
            maxV = np.amax(V)

    

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)

        #ax.set_xlim([xmin, xmax])
        #ax.set_ylim([ymin, ymax])
        ax.set_ylim([minV, maxV])
        D = pp.pload(frame_number+startOffset, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = np.sqrt(D.vx1.T ** 2 + D.vx2.T ** 2 + D.vx3.T ** 2)
      
        im2 = plt.plot(x,V)  # plotting fluid data.
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1 - startOffset)

    #plt.show()

    f = r"velocity_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
