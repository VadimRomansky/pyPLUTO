from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_velocity_animated_1d_3d(ntot, w_dir, unit_density, unit_length, unit_velocity):
    f1 = plt.figure(figsize=[10,8])


    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    xmin = D.x1.min()
    xmax = D.x1.max()
    ymin = D.x2.min()
    ymax = D.x2.max()
    zpoint = math.floor(D.rho.T.shape[0] / 2)
    ypoint = math.floor(D.rho.T.shape[1] / 2)
    print(zpoint)
    Vx = D.vx1.T[zpoint, ypoint, :]
    Vy = D.vx2.T[zpoint, ypoint, :]
    Vz = D.vx3.T[zpoint, ypoint, :]
    V = np.sqrt(Vx ** 2 + Vy ** 2 + Vz ** 2)
    minV = V[0][0]
    maxV = V[0][0]
    xmin = D.x1.min()
    xmax = D.x1.max()
    dx = unit_length * (xmax - xmin) / V.shape[0]
    x = dx * range(V.shape[0])

    for i in range(ntot + 1):
        D = pp.pload(i, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        Vx = D.vx1.T[zpoint, ypoint, :]
        Vy = D.vx2.T[zpoint, ypoint, :]
        Vz = D.vx3.T[zpoint, ypoint, :]
        V = np.sqrt(Vx ** 2 + Vy ** 2 + Vz ** 2)
        if(np.amin(V) < minV):
            minV = np.amin(V)
        if(np.amax(V) > maxV):
            maxV = np.amax(V)


    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_ylim([minV, maxV])
        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        Vx = D.vx1.T[zpoint, ypoint, :]
        Vy = D.vx2.T[zpoint, ypoint, :]
        Vz = D.vx3.T[zpoint, ypoint, :]
        V = np.sqrt(Vx ** 2 + Vy ** 2 + Vz ** 2)
        im2 = plt.plot(x, V)
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"velocity.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
