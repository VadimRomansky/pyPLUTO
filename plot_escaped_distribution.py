import matplotlib.pyplot as plt
from pylab import *
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_escaped_distribution(ns, npr, w_dir, datatype):
    f1 = plt.figure(figsize=[6,6])
    ax = f1.add_subplot(111)

    PVmag1 = np.zeros([npr])
    for i in range(npr):
        PVmag1[i] = -1

    for i in range(ns):
        P = pr.ploadparticles(ns-i, w_dir, datatype=datatype,
                          ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        PVmag = np.sqrt(P.vx1 ** 2 + P.vx2 ** 2 + P.vx3 ** 2)  # estimating the velocity magnitude
        for i in range(len(PVmag)):
            id = int(P.id[i])-1
            if(PVmag1[id] < 0):
                PVmag1[id] = PVmag[i]

    maxU = 0;
    minU = 0;
    if(len(PVmag1) > 0 ):
        maxU = max(PVmag1)
        minU = min(PVmag1)

    #im1 = ax.hist(PVmag, bins=20, range=(0,maxU+1), density=True) # scatter plot
    #ax.set_xlim([0, 1e5])
    y,x = np.histogram(PVmag1, 50, range = (minU, maxU+1), density = True)

    x=x[0:len(x)-1]

    plt.plot(x, y)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('escaped_distribution.png')
    plt.close()