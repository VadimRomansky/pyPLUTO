import math

import numpy as np

def getScalarArray(A, b, excl_axis, point):
    ndim = len(A.shape)

    if(ndim == 1):
        print("cant get 2d array of 1d setup\n")
        return


    if (ndim == 2):
        nx = A.shape[0]
        ny = A.shape[1]
    elif (ndim == 3):
        if (excl_axis == 3):
            nx = A.shape[0]
            ny = A.shape[1]
        elif (excl_axis == 2):
            nx = A.shape[0]
            ny = A.shape[2]
        elif (excl_axis == 1):
            nx = A.shape[1]
            ny = A.shape[2]
        else:
            print("wrong excluded axis\n")
            return
    else:
        print("wrong number of dims\n")
        return

    result = np.zeros([ny, nx])

    if (ndim == 2):
        result = A.T[:, :] * b
    if (ndim == 3):
        if (excl_axis == 3):
            zpoint = math.floor(A.T.shape[0] * point)
            result = A.T[zpoint, :, :] * b
        elif (excl_axis == 2):
            zpoint = math.floor(A.T.shape[1] * point)
            result = A.T[:, zpoint, :] * b
        elif (excl_axis == 1):
            zpoint = math.floor(A.T.shape[2] * point)
            result = A.T[:, :, zpoint] * b
        else:
            print("wrong excluded axis\n")
            return

    np.flip(result, 0)

    return result