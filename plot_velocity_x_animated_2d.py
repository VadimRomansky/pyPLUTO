from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_x_animated_2d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):
    f1 = plt.figure(figsize=[10,8])

    D = pp.pload(ntot, varNames = ['vx1'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    ymin = D.x2.min()*UNIT_LENGTH
    ymax = D.x2.max()*UNIT_LENGTH
    V=D.vx1.T

    minV = V[0][0]
    maxV = V[0][0]

    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx1'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = D.vx1.T;
        if (np.amin(V) < minV):
            minV = np.amin(V)
        if (np.amax(V) > maxV):
            maxV = np.amax(V)


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])
        D = pp.pload(frame_number, varNames = ['vx1'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = D.vx1.T
        im2 = ax.imshow(V, origin='upper', aspect = 'auto',
                        extent=[xmin, xmax, ymin, ymax])  # plotting fluid data.
        im2.set_clim(minV, maxV)
        plt.colorbar(im2, cax=cax2, orientation='horizontal')  # vertical colorbar for fluid data.
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"velocityX_2d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
