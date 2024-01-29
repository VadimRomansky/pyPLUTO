from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_field(ns, w_dir):
    f1 = plt.figure(figsize=[6,6])
    ax = f1.add_subplot(111)

    D = pp.pload(ns, varNames = ['Bx1','Bx2','Bx3'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    #B = D.Bx1.T**2 + D.Bx2.T**2 + D.Bx3.T**2
    nx = shape(D.Bx1.T)[0]
    ny = shape(D.Bx1.T)[1]
    B = np.zeros([nx,ny])
    for i in range(nx):
        for j in range(ny):
            B[i][j] = np.sqrt(D.Bx1.T[i][j]**2 + D.Bx2.T[i][j]**2 + D.Bx3.T[i][j]**2)

    im2 = ax.imshow(B, origin='upper',extent=[D.x1.min(), D.x1.max(), D.x2.min(), D.x2.max()]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.75,0.03])
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis',fontsize=18)
    ax.set_ylabel(r'Y-axis',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig('field.png')