from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_density_average(ntot, w_dir):

    D = pp.pload(ntot, varNames = ['rho'], w_dir = w_dir, datatype='dbl') # Load fluid data.
    V=D.rho.T
    Va = np.zeros(V.shape[1])

    xmin = D.x1.min()
    xmax = D.x1.max()
    ymin = D.x2.min()
    ymax = D.x2.max()

    
    for i in range(V.shape[1]):
    	for j in range(V.shape[0]):
    		Va[i] = Va[i]+V[j][i]/V.shape[0]
    		
    plt.plot(Va)
    plt.show()

    
