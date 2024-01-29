from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_animated_1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure()


    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl')
    V = D.rho.T*unit_density
    xmin = D.x1.min()
    xmax = D.x1.max()
    ymin = D.x2.min()
    ymax = D.x2.max()
    xmin = D.x1.min() * unit_length
    xmax = D.x1.max() * unit_length
    dx = (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)

        D = pp.pload(frame_number, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V=D.rho.T*unit_density
        Va = np.zeros(V.shape[1])

        for i in range(V.shape[1]):
            for j in range(V.shape[0]):
                Va[i] = Va[i] + V[j][i] / V.shape[0]
        ax.set_xlabel(r'R', fontsize=18)
        ax.set_ylabel(r'rho', fontsize=18)
        ax.minorticks_on()

        im2 = plt.plot(x, Va)  # plotting fluid data.
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"density_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
