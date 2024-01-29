from matplotlib import animation
import matplotlib.colors as colors
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_density_animated_3d_slice2d_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VLOCITY, xmin, xmax, ymin, ymax):
    f1 = plt.figure()

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0]/2)
    print(zpoint)
    V=D.rho.T[zpoint,:,:]

    #ax.set_xlim([xmin, xmax])
    #ax.set_ylim([ymin, ymax])
    
    minRho = V[0][0]
    maxRho = V[0][0]

    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V=D.rho.T[zpoint,:,:]
        if (np.amin(V) < minRho):
            minRho = np.amin(V)
        if (np.amax(V) > maxRho):
            maxRho = np.amax(V)


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        D = pp.pload(frame_number, varNames = ['rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V=D.rho.T[zpoint,:,:]
        im2 = ax.imshow(V, origin='upper', norm = colors.LogNorm(vmin = minRho, vmax = maxRho), aspect = 'auto',
                        extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH])  # plotting fluid data.
        plt.colorbar(im2, orientation='horizontal')  # vertical colorbar for fluid data.
        ax.set_xlabel(r'X-axis', fontsize=14)
        ax.set_ylabel(r'Y-axis', fontsize=14)
        ax.minorticks_on()
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"density_3d_to_2d_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
