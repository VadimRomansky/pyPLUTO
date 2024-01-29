from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_gamma(ns, w_dir, datatype):
    f1 = plt.figure(figsize=[6,6])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    #B = D.Bx1.T**2 + D.Bx2.T**2 + D.Bx3.T**2
    nx = shape(D.vx1.T)[0]
    ny = shape(D.vx1.T)[1]
    V = np.zeros([nx,ny])
    for i in range(nx):
        for j in range(ny):
            V[i][j] = np.log10(1.0/np.sqrt(1.0 - D.vx1.T[i][j]**2 - D.vx2.T[i][j]**2 - D.vx3.T[i][j]**2))
    ratio = 0.1 #from 0.5
    V1=V[int((0.5 - ratio)*nx):int((0.5 + ratio)*nx),int((0.5 - ratio)*ny):int((0.5 + ratio)*ny)]
    print(np.amax(V1))
    im2 = ax.imshow(V1, origin='upper',extent=[ratio*D.x1.min(), ratio*D.x1.max(), ratio*D.x2.min(), ratio*D.x2.max()]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.75,0.03])
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis',fontsize=18)
    ax.set_ylabel(r'Y-axis',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('gamma.png')