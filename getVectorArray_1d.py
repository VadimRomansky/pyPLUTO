import math

import numpy as np

def getVectorArray_1d(A1, A2, A3, b, axis, point1, point2):
    ndim = len((A1.shape))

    nx = A1.shape[0]
    V = np.zeros([axis-1])

    if (ndim == 1):
        if(axis != 1):
            print("wrong axis\n")
            return
        Vz = A3[:] * b
        Vy = A2[:] * b
        Vx = A1[:] * b
        V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
    if (ndim == 2):
        if(axis == 1):
            ypoint = math.floor(A1.shape[1] *point1)
            Vz = A3[:, ypoint] * b
            Vy = A2[:, ypoint] * b
            Vx = A1[:, ypoint] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(axis == 2):
            xpoint = math.floor(A1.shape[0] *point1)
            Vz = A3[xpoint, :] * b
            Vy = A2[xpoint, :] * b
            Vx = A1[xpoint, :] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        else:
            print("wrong axis\n")
            return
    if (ndim == 3):
        if(axis == 1):
            ypoint = math.floor(A1.shape[1] *point1)
            zpoint = math.floor(A1.shape[2] *point1)
            Vz = A3[:, ypoint, zpoint] * b
            Vy = A2[:, ypoint, zpoint] * b
            Vx = A1[:, ypoint, zpoint] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(axis == 2):
            xpoint = math.floor(A1.shape[0] *point1)
            zpoint = math.floor(A1.shape[2] *point1)
            Vz = A3[xpoint,:, zpoint] * b
            Vy = A2[xpoint,:, zpoint] * b
            Vx = A1[xpoint,:, zpoint] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        elif(axis == 3):
            xpoint = math.floor(A1.shape[0] *point1)
            ypoint = math.floor(A1.shape[1] *point1)
            Vz = A3[xpoint, ypoint, :] * b
            Vy = A2[xpoint, ypoint, :] * b
            Vx = A1[xpoint, ypoint, :] * b
            V = np.sqrt(np.square(Vx) + np.square(Vy) + np.square(Vz))
        else:
            print("wrong axis")
            return

    return V