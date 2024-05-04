from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d

def plot_energy(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype):
    c = 2.998E10
    gam = 5.0/3.0
    mp = 1.6E-24
    fracHe = 0.1
    mu = (mp + fracHe * 4*mp) /(2.0 + 3.0 * fracHe)

    UNIT_FIELD = np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)
    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho','Bx1','Bx2','Bx3'], w_dir=w_dir, datatype=datatype)

    ndim = len(D.vx1.shape)
    E = np.zeros([ntot+1])
    Ekin = np.zeros([ntot+1])
    Etherm = np.zeros([ntot+1])
    Emag = np.zeros([ntot+1])
    mass = np.zeros([ntot+1])

    Vcell = np.zeros(D.vx1.shape)

    for i in range(D.vx1.shape[0]):
        dVx = 1.0
        if (D.geometry == 'CARTESIAN'):
            dVx = D.dx1[i]
        elif (D.geometry == 'CYLINDRICAL'):
            dVx = D.x1[i] * D.dx1[i]
        elif (D.geometry == 'POLAR'):
            dVx = D.x1[i] * D.dx1[i]
        elif (D.geometry == 'SPHERICAL'):
            dVx = D.x1[i] * D.x1[i] * D.dx1[i]

        if (ndim > 1):
            for j in range(D.vx1.shape[1]):

                dVy = 1.0
                if (D.geometry == 'CARTESIAN'):
                    dVy = D.dx2[j]
                elif (D.geometry == 'CYLINDRICAL'):
                    dVy = D.dx2[j]
                elif (D.geometry == 'POLAR'):
                    dVy = D.dx2[j]
                elif (D.geometry == 'SPHERICAL'):
                    dVy = np.sin(D.x2[j]) * D.dx2[j]

                if (ndim > 2):
                    for k in range(D.vx1.shape[2]):

                        dVz = 1.0
                        if (D.geometry == 'CARTESIAN'):
                            dVz = D.dx3[k]
                        elif (D.geometry == 'CYLINDRICAL'):
                            dVz = D.dx3[k]
                        elif (D.geometry == 'SPHERICAL'):
                            dVz = D.dx3[k]

                        Vcell[i][j][k] = dVx * dVy * dVz

                else:
                    if (D.geometry == 'CARTESIAN'):
                        dVy = dVy
                    elif (D.geometry == 'CYLINDRICAL'):
                        dVy = dVy * 2 * np.pi
                    elif (D.geometry == 'SPHERICAL'):
                        dVy = dVy * 2 * np.pi

                    Vcell[i][j] = dVx * dVy
        else:

            if (D.geometry == 'CARTESIAN'):
                dVx = dVx
            elif (D.geometry == 'CYLINDRICAL'):
                dVx = dVx * 2 * np.pi
            elif (D.geometry == 'POLAR'):
                dVx = dVx * 2 * np.pi
            elif (D.geometry == 'SPHERICAL'):
                dVx = dVx * 4 * np.pi

            Vcell[i] = dVx

    for n in range(ntot+1):
        D = pp.pload(n, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho', 'Bx1', 'Bx2', 'Bx3'], w_dir=w_dir,
                     datatype=datatype)
        Ekin[n] = np.sum(D.rho*c*c*(1.0/np.sqrt(1.0 - (D.vx1*D.vx1 + D.vx2*D.vx2+D.vx3*D.vx3)*UNIT_VELOCITY*UNIT_VELOCITY/(c*c))-1.0)*UNIT_DENSITY*Vcell*UNIT_LENGTH*UNIT_LENGTH*UNIT_LENGTH)
        Etherm[n] = np.sum((D.prs*UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY/(gam-1.0))*Vcell*UNIT_LENGTH*UNIT_LENGTH*UNIT_LENGTH)
        Emag[n] = np.sum(((D.Bx1*D.Bx1 + D.Bx2*D.Bx2 + D.Bx3*D.Bx3)/(8*np.pi))*UNIT_FIELD*UNIT_FIELD*Vcell*UNIT_LENGTH*UNIT_LENGTH*UNIT_LENGTH)

        # for i in range(D.vx1.shape[0]):
        #
        #     dVx = 1.0
        #     if(D.geometry == 'CARTESIAN'):
        #         dVx = D.dx1[i]*UNIT_LENGTH
        #     elif(D.geometry == 'CYLINDRICAL'):
        #         dVx = D.x1[i]*D.dx1[i]*UNIT_LENGTH*UNIT_LENGTH
        #     elif(D.geometry == 'POLAR'):
        #         dVx = D.x1[i] * D.dx1[i] * UNIT_LENGTH * UNIT_LENGTH
        #     elif(D.geometry == 'SPHERICAL'):
        #         dVx = D.x1[i]*D.x1[i]*D.dx1[i]*UNIT_LENGTH*UNIT_LENGTH*UNIT_LENGTH
        #
        #
        #     if(ndim > 1):
        #         for j in range(D.vx1.shape[1]):
        #
        #             dVy = 1.0
        #             if(D.geometry == 'CARTESIAN'):
        #                 dVy = D.dx2[j]*UNIT_LENGTH
        #             elif(D.geometry == 'CYLINDRICAL'):
        #                 dVy = D.dx2[j]*UNIT_LENGTH
        #             elif (D.geometry == 'POLAR'):
        #                 dVy = D.dx2[j]
        #             elif(D.geometry == 'SPHERICAL'):
        #                 dVy = np.sin(D.x2[j])*D.dx2[j]
        #
        #             if(ndim > 2):
        #                 for k in range(D.vx1.shape[2]):
        #
        #                     dVz = 1.0
        #                     if(D.geometry == 'CARTESIAN'):
        #                         dVz = D.dx3[k]*UNIT_LENGTH
        #                     elif(D.geometry == 'CYLINDRICAL'):
        #                         dVz = D.dx3[k]
        #                     elif(D.geometry == 'SPHERICAL'):
        #                         dVz = D.dx3[k]
        #
        #                     V2 = (D.vx1[i][j][k] * D.vx1[i][j][k] + D.vx2[i][j][k] * D.vx2[i][j][k] + D.vx3[i][j][k] * D.vx3[i][j][k]) * UNIT_VELOCITY * UNIT_VELOCITY
        #                     gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
        #                     Ekin[n] = Ekin[n] + D.rho[i][j][k] * UNIT_DENSITY * (gamma - 1.0)*c*c * dVx*dVy*dVz
        #                     Etherm[n] = Etherm[n] + (1.0/(gam-1))*(D.prs[i][j][k]*UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY)*dVx*dVy*dVz
        #                     #Emag[n] = Emag[n] + ((D.Bx1[i][j][k] * D.Bx1[i][j][k] + D.Bx2[i][j][k] * D.Bx2[i][j][k] + D.Bx3[i][j][k] *D.Bx3[i][j][k]) *UNIT_FIELD*UNIT_FIELD/ (8 * np.pi)) * dVx*dVy*dVz
        #
        #                     mass[n] = mass[n] + D.rho[i][j][k]*UNIT_DENSITY*dVx*dVy*dVz
        #             else:
        #
        #                 if (D.geometry == 'CARTESIAN'):
        #                     dVy = dVy
        #                 elif (D.geometry == 'CYLINDRICAL'):
        #                     dVy = dVy*2*np.pi
        #                 elif (D.geometry == 'SPHERICAL'):
        #                     dVy = dVy*2*np.pi
        #
        #                 V2 = (D.vx1[i][j] * D.vx1[i][j] + D.vx2[i][j] * D.vx2[i][j] + D.vx3[i][j] * D.vx3[i][j]) * UNIT_VELOCITY * UNIT_VELOCITY
        #                 gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
        #                 Ekin[n] = Ekin[n] + D.rho[i][j] * UNIT_DENSITY * (gamma - 1.0)*c*c * dVx*dVy
        #                 Etherm[n] = Etherm[n] + (1.0/(gam-1.0))*(D.prs[i][j]*UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY)*dVx*dVy
        #                 #Emag[n] = Emag[n] + ((D.Bx1[i][j] * D.Bx1[i][j] + D.Bx2[i][j] * D.Bx2[i][j] + D.Bx3[i][j] * D.Bx3[i][j]) *UNIT_FIELD*UNIT_FIELD / (8 * np.pi)) * dVx*dVy
        #
        #                 mass[n] = mass[n] + D.rho[i][j]*UNIT_DENSITY*dVx*dVy
        #     else:
        #
        #         if (D.geometry == 'CARTESIAN'):
        #             dVx = dVx
        #         elif (D.geometry == 'CYLINDRICAL'):
        #             dVx = dVx*2*np.pi
        #         elif(D.geometry == 'POLAR'):
        #             dVx = dVx*2*np.pi
        #         elif (D.geometry == 'SPHERICAL'):
        #             dVx = dVx*4*np.pi
        #
        #         V2 = (D.vx1[i]*D.vx1[i] + D.vx2[i]*D.vx2[i] + D.vx3[i]*D.vx3[i])*UNIT_VELOCITY*UNIT_VELOCITY
        #         gamma = 1.0/np.sqrt(1.0 - V2/(c*c))
        #         Ekin[n] = Ekin[n] + D.rho[i]*UNIT_DENSITY*(gamma - 1.0)*c*c*dVx
        #         Etherm[n] = Etherm[n] + (1.0/(gam-1.0))*(D.prs[i])*UNIT_DENSITY*UNIT_VELOCITY*UNIT_VELOCITY*dVx
        #         #Emag[n] = Emag[n] + ((D.Bx1[i]*D.Bx1[i]+D.Bx2[i]*D.Bx2[i]+D.Bx3[i]*D.Bx3[i]) *UNIT_FIELD*UNIT_FIELD/(8*np.pi))*dVx
        #
        #         mass[n] = mass[n] + D.rho[i]*UNIT_DENSITY*dVx

    for n in range(ntot+1):
        E[n] = Ekin[n] + Etherm[n] + Emag[n]

    max = 2*np.amax(E)
    min = max/1E10

    t = np.zeros([ntot+1])
    for n in range(ntot+1):
        t[n] = n

    im2 = plt.plot(t, E, 'r-', t, Ekin, 'g-', t, Etherm, 'y-',t, Emag, 'b-')  # plotting fluid data.
    ax.legend(['full energy', 'kinetic energy', 'thermal energy', 'magnetic energy'])
    ax.set_yscale("log")
    ax.set_ylim([min,max])
    plt.savefig('energy.png')
    plt.close()