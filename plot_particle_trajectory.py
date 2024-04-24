from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation
def plot_particle_trajectory(ntot, npar, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    f1 = plt.figure(figsize=[10,8])
    ax = f1.add_subplot(111)

    
    coord = np.zeros([2,ntot+1]);

    P = pr.ploadparticles(0, w_dir, datatype=datatype, ptype='CR')
    number = P.id[npar];

    for j in range(ntot+1):
        P = pr.ploadparticles(j, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt
        for i in range(len(P.id)):
    	    if(number == P.id[i]):
    	        coord[0][j] = P.x1[i]*UNIT_LENGTH
    	        coord[1][j] = P.x2[i]*UNIT_LENGTH

    plt.plot(coord[0],coord[1])

    print(coord)


    cax2 = f1.add_axes([0.125, 0.92, 0.75, 0.03])


    print(w_dir)
    D = pp.pload(ntot, varNames = ['Bx1', 'Bx2', 'Bx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    V = np.sqrt(D.Bx1.T ** 2 + D.Bx2.T ** 2 + D.Bx3.T ** 2)
    #im2 = ax.imshow(V, origin='lower',extent=[D.x1.min(), D.x1.max(), D.x2.min(), D.x2.max()]) # plotting fluid data.
    #plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'x',fontsize=18)
    ax.set_ylabel(r'y',fontsize=18)
    ax.minorticks_on()
    #plt.show()
    plt.savefig('particle_trajectory.png')
    plt.close()


    
