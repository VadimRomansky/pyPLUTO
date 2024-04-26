from matplotlib import animation
from pylab import *
import pyPLUTO.pload as pp  # importing the pyPLUTO pload module.
import pyPLUTO.ploadparticles as pr  # importing the pyPLUTO ploadparticles module.
from matplotlib.animation import FuncAnimation

from getScalarArray_1d import getScalarArray_1d
from getVectorArray_1d import getVectorArray_1d

def plot_energy(ntot, w_dir, UNIT_DENSITY, UNIT_LENGTH, UNIT_VELOCITY, datatype, geom = 'cartesian'):
    c = 2.998E10
    UNIT_FIELD = np.sqrt(4 * np.pi * UNIT_DENSITY * UNIT_VELOCITY * UNIT_VELOCITY)
    f1 = plt.figure(figsize=[10, 8])
    ax = f1.add_subplot(111)
    D = pp.pload(ntot, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho','Bx1','Bx2','Bx3'], w_dir=w_dir, datatype=datatype)

    ndim = len(D.vx1.shape)
    E = np.zeros([ntot+1])
    Ekin = np.zeros([ntot+1])
    Emag = np.zeros([ntot+1])

    for n in range(ntot+1):
        D = pp.pload(n, varNames=['vx1', 'vx2', 'vx3', 'prs', 'rho', 'Bx1', 'Bx2', 'Bx3'], w_dir=w_dir,
                     datatype=datatype)
        for i in range(D.vx1.shape[0]):

            dVx = 1.0
            if(geom == 'cartesian'):
                dVx = D.dx1[i]*UNIT_LENGTH
            elif(geom == 'cylindrical'):
                dVx = D.x1[i]*D.dx1[i]*UNIT_LENGTH*UNIT_LENGTH
            elif(geom == 'spherical'):
                dVx = D.x1[i]*D.x1[i]*D.dx1[i]*UNIT_LENGTH*UNIT_LENGTH*UNIT_LENGTH


            if(ndim > 1):
                for j in range(D.vx1.shape[1]):

                    dVy = 1.0
                    if(geom == 'cartesian'):
                        dVy = D.dx2[j]*UNIT_LENGTH
                    elif(geom == 'cylindrical'):
                        dVy = D.dx2[j]*UNIT_LENGTH
                    elif(geom == 'spherical'):
                        dVy = np.sin(D.x2[j])*D.dx2[j]

                    if(ndim > 2):
                        for k in range(D.vx1.shape[2]):

                            dVz = 1.0
                            if(geom == 'cartesian'):
                                dVz = D.dx3[k]*UNIT_LENGTH
                            elif(geom == 'cylidrical'):
                                dVz = D.dx3[k]
                            elif(geom == 'spherical'):
                                dVz = D.dx3[k]

                            V2 = (D.vx1[i][j][k] * D.vx1[i][j][k] + D.vx2[i][j][k] * D.vx2[i][j][k] + D.vx3[i][j][k] * D.vx3[i][j][k]) * UNIT_VELOCITY * UNIT_VELOCITY
                            gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
                            Ekin[n] = Ekin[n] + D.rho[i][j][k] * UNIT_DENSITY * (gamma - 1.0) * dVx*dVy*dVz
                            Emag[n] = Emag[n] + ((D.Bx1[i][j][k] * D.Bx1[i][j][k] + D.Bx2[i][j][k] * D.Bx2[i][j][k] + D.Bx3[i][j][k] *D.Bx3[i][j][k]) *UNIT_FIELD*UNIT_FIELD/ (8 * np.pi)) * dVx*dVy*dVz
                    else:
                        V2 = (D.vx1[i][j] * D.vx1[i][j] + D.vx2[i][j] * D.vx2[i][j] + D.vx3[i][j] * D.vx3[i][j]) * UNIT_VELOCITY * UNIT_VELOCITY
                        gamma = 1.0 / np.sqrt(1.0 - V2 / (c * c))
                        Ekin[n] = Ekin[n] + D.rho[i][j] * UNIT_DENSITY * (gamma - 1.0) * dVx*dVy
                        Emag[n] = Emag[n] + ((D.Bx1[i][j] * D.Bx1[i][j] + D.Bx2[i][j] * D.Bx2[i][j] + D.Bx3[i][j] * D.Bx3[i][j]) *UNIT_FIELD*UNIT_FIELD / (8 * np.pi)) * dVx*dVy
            else:
                V2 = (D.vx1[i]*D.vx1[i] + D.vx2[i]*D.vx2[i] + D.vx3[i]*D.vx3[i])*UNIT_VELOCITY*UNIT_VELOCITY
                gamma = 1.0/np.sqrt(1.0 - V2/(c*c))
                Ekin[n] = Ekin[n] + D.rho[i]*UNIT_DENSITY*(gamma - 1.0)*dVx
                Emag[n] = Emag[n] + ((D.Bx1[i]*D.Bx1[i]+D.Bx2[i]*D.Bx2[i]+D.Bx3[i]*D.Bx3[i]) *UNIT_FIELD*UNIT_FIELD/(8*np.pi))*dVx

    for n in range(ntot+1):
        E[n] = Ekin[n] + Emag[n]

    t = np.zeros([ntot+1])
    for n in range(ntot+1):
        t[n] = n

    im2 = plt.plot(t, E, 'r-', t, Ekin, 'g-', t, Emag, 'b-')  # plotting fluid data.
    ax.legend(['full enrgy', 'kinetic energy', 'magnetic energy'])
    ax.set_yscale("log")
    plt.savefig('energy.png')
    plt.close()