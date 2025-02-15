import numpy as np
from matplotlib.animation import FuncAnimation
from pylab import *
from matplotlib import animation
import pyPLUTO.pload as pp # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr # importing the pyPLUTO ploadparticles module.
def plot_kinetic_distribution_animated_window(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, xmin, xmax, ymin, ymax, zmin, zmax, datatype, file_name = 'distribution_kinetic_window.gif', out_dir = ""):
    plt.rcParams.update({'font.size': 15})
    #plt.rcParams['text.usetex'] = True
    f1 = plt.figure(figsize=[6,6])
    plt.rcParams["figure.dpi"] = 200
    ax = f1.add_subplot(111)
    P = pr.ploadparticles(ntot, w_dir, datatype=datatype,ptype='CR') # Loading particle data : particles.00ns_ch00.flt

    Nmomentum = len(P.p[0])
    F = np.zeros([Nmomentum])
    p = P.p[0]
    V = 0

    for i in range(len(P.id)):
        if ((P.x[i] >= xmin) and (P.x[i] <= xmax) and (P.y[i] >= ymin) and (P.y[i] <= ymax) and (P.z[i] >= zmin) and (P.z[i] <= zmax)):
            for j in range(Nmomentum):
                F[j] = F[j] + P.F[i][j]*P.dV[i]
                V = V + P.dV[i]

    for j in range(Nmomentum):
        if(F[j] <= 0):
            F[j] = 1E-100
    #for i in range(len(y)):
        #y = y/PVmag[i]
    minF = np.amin(F)
    maxF = np.amax(F)

    Fa = np.zeros([Nmomentum])

    Fa[0] = F[0]

    for i in range(Nmomentum):
        Fa[i] = F[0] * (p[0] / p[i]) ** 4

    for i in range(ntot+1):
        P = pr.ploadparticles(i, w_dir, datatype=datatype,
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        F = np.zeros([Nmomentum])
        V = 0

        for k in range(len(P.id)):
            if ((P.x[k] >= xmin) and (P.x[k] <= xmax) and (P.y[k] >= ymin) and (P.y[k] <= ymax) and (P.z[k] >= zmin) and (P.z[k] <= zmax)):
                for j in range(Nmomentum):
                    F[j] = F[j] + P.F[k][j] * P.dV[k]
                    V = V + P.dV[k]

        for j in range(Nmomentum):
            if (F[j] <= 0):
                F[j] = 1E-100

        if(np.amin(F) < minF):
            minF = np.amin(F)
        if(np.amax(F) > maxF):
            maxF = np.amax(F)

    def update(frame_number):
        f1.clear()
        ax = f1.add_subplot(111)
        ax.set_xscale("log")
        ax.set_yscale("log")
        #ax.set_xlim([1E3, 1E8])
        #ax.set_ylim([minF, maxF])
        ax.set_ylim([1E-16, 1E1])
        P = pr.ploadparticles(frame_number, w_dir, datatype=datatype,
                              ptype='CR')  # Loading particle data : particles.00ns_ch00.flt

        F = np.zeros([Nmomentum])
        V = 0

        for k in range(len(P.id)):
            for j in range(Nmomentum):
                F[j] = F[j] + P.F[k][j] * P.dV[k]
                V = V + P.dV[k]
        for j in range(Nmomentum):
            if (F[j] <= 0):
                F[j] = 1E-100

        im1 = ax.plot(p, F)
        ax.plot(p, Fa)

        return im1

    anim = FuncAnimation(f1, update, interval=10, frames=ntot + 1)

    # plt.show()

    f = out_dir + file_name
    writergif = animation.PillowWriter(fps=4)
    anim.save(f, writer=writergif)
    plt.close()