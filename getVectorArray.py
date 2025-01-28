import math

import numpy as np

def getVectorArray(A1, A2, A3, b, excl_axis, point):
    ndim = len(A1.shape)

    if(ndim == 1):
        print("cant get 2d array of 1d setup\n")
        return

    if(ndim == 2):
        nx = A1.shape[0]
        ny = A1.shape[1]
    elif(ndim == 3):
        if(excl_axis == 3):
            nx = A1.shape[0]
            ny = A1.shape[1]
        elif(excl_axis == 2):
            nx = A1.shape[0]
            ny = A1.shape[2]
        elif(excl_axis == 1):
            nx = A1.shape[1]
            ny = A1.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return

    V = np.zeros([ny,nx])

    if(ndim == 2):
        Vz = A3.T[:, :] * b
        Vy = A2.T[:, :] * b
        Vx = A1.T[:, :] * b
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if(ndim == 3):
        if(excl_axis == 3):
            zpoint = math.floor(A1.T.shape[0]* point)
            Vz = A3.T[zpoint, :, :] * b
            Vy = A2.T[zpoint, :, :] * b
            Vx = A1.T[zpoint, :, :] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(excl_axis == 2):
            zpoint = math.floor(A1.T.shape[1]* point)
            Vz = A3.T[:,zpoint, :] * b
            Vy = A2.T[:,zpoint, :] * b
            Vx = A1.T[:,zpoint, :] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(excl_axis == 1):
            zpoint = math.floor(A1.T.shape[2]* point)
            Vz = A3.T[:,:,zpoint] * b
            Vy = A2.T[:,:,zpoint] * b
            Vx = A1.T[:,:,zpoint] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        else:
            print("wrong excluded axis\n")
            return
    np.flip(V,0)

    return V