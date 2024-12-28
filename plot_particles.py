from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_particles(ns, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, file_name = 'particles.png'):
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 500
    plt.rcParams['axes.linewidth'] = 0.1
    ax = f1.add_subplot(111)
    P = pr.ploadparticles(ns, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    PVmag = np.sqrt(P.vx1**2 + P.vx2**2 + P.vx3**2) # estimating the velocity magnitude

    im1 = ax.scatter(P.x1*UNIT_LENGTH, P.x2*UNIT_LENGTH, s=10, c=PVmag, cmap=plt.get_cmap('hot')) # scatter plot

    cax1 = f1.add_axes([0.91,0.12,0.03,0.75])
    plt.colorbar(im1,cax=cax1) # vertical colorbar for particle data.
    D = pp.pload(ns, varNames = ['vx1','vx2','vx3'], w_dir = w_dir, datatype=datatype) # Load fluid data.
    im2 = ax.imshow(D.vx1.T, origin='upper',extent=[D.x1.min()*UNIT_LENGTH, D.x1.max()*UNIT_LENGTH, D.x2.min()*UNIT_LENGTH, D.x2.max()*UNIT_LENGTH]) # plotting fluid data.
    cax2 = f1.add_axes([0.125,0.92,0.75,0.03])
    plt.colorbar(im2,cax=cax2,orientation='horizontal') # vertical colorbar for fluid data.
    ax.set_xlabel(r'X-axis',fontsize=18)
    ax.set_ylabel(r'Y-axis',fontsize=18)
    ax.minorticks_on()
    #plt.axis([0.0,1.0,0.0,1.0])
    plt.savefig(file_name)
    plt.close()