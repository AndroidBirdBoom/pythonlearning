import numpy as np
from numpy import *

if __name__ == "__main__":
    d = eye(4)
    print(type(d))
    print(d)
    print('shape' in dir(d))
    print(d.shape)
    print(d[::2])
    ar = np.array([1, 2, 3, 4, 5, 6], dtype=float_)
    print(ar, ar.shape)
    ar2 = np.array([[1, 2], [3, 4], [5, 6]])
    print(ar2, ar2.shape)
    ar3 = np.array([1, ])
    print(ar3, ar3.shape)

    dt = np.dtype(np.int32)
    print(dt)

    my_arrays = np.zeros((5, 3))
    print(my_arrays)
    my_new_arrays = np.ones((3, 2))
    print(my_new_arrays)
    my_random_arrays = np.random.random((3, 4))
    print(my_random_arrays)
