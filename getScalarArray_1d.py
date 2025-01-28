import math

import numpy as np

def getScalarArray_1d(A, b, axis, point1, point2):
    ndim = len((A.shape))

    minRho = 0
    maxRho = 0

    nx = A.shape[0]
    result = np.zeros([A.shape[axis-1]])

    if (ndim == 1):
        if (axis != 1):
            print("wrong axis\n")
            return
        result = A[:] * b
    if (ndim == 2):
        if (axis == 1):
            ypoint = math.floor(A.shape[1] * point1)
            result = A[:, ypoint] * b
        elif (axis == 2):
            xpoint = math.floor(A.shape[0] * point1)
            result = A[xpoint, :] * b
        else:
            print("wrong axis\n")
            return
    if (ndim == 3):
        if (axis == 1):
            ypoint = math.floor(A.shape[1] * point1)
            zpoint = math.floor(A.shape[2] * point2)
            result = A[:, ypoint, zpoint] * b
        elif (axis == 2):
            xpoint = math.floor(A.shape[0] * point1)
            zpoint = math.floor(A.shape[2] * point2)
            result = A[xpoint, :, zpoint] * b
        elif (axis == 3):
            xpoint = math.floor(A.shape[0] * point1)
            ypoint = math.floor(A.shape[1] * point2)
            result = A[xpoint, ypoint, :] * b

    return result