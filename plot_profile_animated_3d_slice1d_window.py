from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_profile_animated_3d_slice1d_window(ntot, w_dir, unit_density, unit_length, unit_velocity, xmin, xmax):
    f1 = plt.figure(figsize=[10,8])

    
    D = pp.pload(ntot, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    zpoint = math.floor(D.rho.T.shape[0] / 2)
    ypoint = math.floor(D.rho.T.shape[1] / 2)
    V = np.abs(D.vx1.T[zpoint,ypoint,:])
    P = D.prs.T[zpoint,ypoint,:]
    rho = D.rho.T[zpoint,ypoint,:]

    xmin1 = D.x1.min()
    xmax1 = D.x1.max()
    dx = unit_length * (xmax1 - xmin1) / V.shape[0]
    x = dx * range(V.shape[0]) + xmin1 * unit_length

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

    

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_yscale("log")
        ax.set_ylim([1E-5,1E11])

        D = pp.pload(frame_number, varNames = ['vx1','vx2','vx3','prs','rho'], w_dir = w_dir, datatype='dbl')  # Load fluid data.
        V = np.abs(D.vx1.T[zpoint, ypoint, :])
        P = D.prs.T[zpoint, ypoint, :]
        rho = D.rho.T[zpoint, ypoint, :]
        x1 = x[N1:N2]
        V1 = V[N1:N2]
        P1 = P[N1:N2]
        rho1 = rho[N1:N2]
      
        im2 = plt.plot(x1,V1,'r-',x1,P1,'g-',x1,rho1,'b-')
        ax.legend(['vx', 'pressure', 'density'])
        return im2

    anim = FuncAnimation(f1, update, interval=10, frames = ntot+1)

    #plt.show()

    f = r"profile_3d_to_1d_window.gif"
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
