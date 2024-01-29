from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_density_2d_average1d(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY):

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V=D.rho.T
    Va = np.zeros(V.shape[1])

    xmin = D.x1.min()*UNIT_LENGTH
    xmax = D.x1.max()*UNIT_LENGTH
    ymin = D.x2.min()*UNIT_LENGTH
    ymax = D.x2.max()*UNIT_LENGTH

    
    for i in range(V.shape[1]):
    	for j in range(V.shape[0]):
    		Va[i] = Va[i]+V[j][i]/V.shape[0]
    		
    plt.plot(Va)
    #plt.show()
    plt.savefig('density_2d_average_1d.png')


    
