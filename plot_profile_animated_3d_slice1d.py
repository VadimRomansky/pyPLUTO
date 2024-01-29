from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_profile_animated_3d_slice1d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])
    
    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0] / 2)
    ypoint = math.floor(D.rho.T.shape[1] / 2)
    V = np.abs(D.vx1.T[zpoint,ypoint,:])
    P = D.prs.T[zpoint,ypoint,:]
    rho = D.rho.T[zpoint,ypoint,:]

    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length * (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin * unit_length
    N1 = int(0.125 * V.shape[0])
    N2 = int(0.275 * V.shape[0])

    

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)

        ax.set_yscale("log")
        ax.set_ylim([1E-5,1E11])

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = np.abs(D.vx1.T[zpoint, ypoint, :])
        P = D.prs.T[zpoint, ypoint, :]
        rho = D.rho.T[zpoint, ypoint, :]
      
        im2 = plt.plot(x,V,'r-',x,P,'g-',x,rho,'b-')  # plotting fluid data.
        ax.legend(['vx', 'pressure', 'density'])
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"profile_3d_to_1d.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
