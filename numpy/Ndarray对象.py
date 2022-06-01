import numpy as np
from numpy import *
import matplotlib.pyplot as plt

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
    print(my_random_arrays.shape)

    my_int_array = np.array([[1, 2], [3, 4]])
    print(my_int_array)
    print(my_int_array[:, 0])

    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    b = np.array([[5., 6.], [7., 8.]])
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a.dot(b))

    c = np.arange(5)
    print(c)
    c = np.array((1, 3, 6))
    print(c, c.shape)

    a = np.array([[11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35]])
    print(a[2, 4])
    print(a[0, 1:4])
    print(a[1:4, 0])
    print(a[::2, ::2])
    print(a[:, 1])
    print(a[1:4, 1:4])
    print(type(a))
    print(a.dtype)
    print(a.size)
    print(a.shape)
    print(a.itemsize)
    print(a.ndim)
    print(a.nbytes)

    b = a[1:4, 1:4]

    print(b)
    print('========================')
    print(b[b != 23])
    print('========================')

    a = a.reshape((1, 25))
    print(a)

    a = np.arange(25)
    print(a)
    a = a.reshape((5, 5))
    print(a)

    b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
                  4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
                  56, 3, 56, 44, 78])
    print(b.size)
    b = b.reshape((5, 5))
    print(b, b.ndim)
    print(a * b)
    c = a.dot(b)
    print(type(c))
    print(a > b)

    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])
    b = b.reshape((3, 1))
    print(a, b, a.dot(b))

    a = np.arange(12)
    print(a.sum(), a.min(), a.max(), a.cumsum())
    print(a, a.shape)
    a = a.reshape((4, 3))
    print(a)

    print(a.sum(), a.min(), a.max(), a.cumsum())

    a = np.arange(0, 100, 10)
    print(a)
    indices = [1, 5, -1]
    b = a[indices]
    print(b, type(b))

    a = np.arange(25)
    a = a.reshape((5, 5))
    print(a)
    b = a[1:4, 1:4]
    print(b)

    a = np.linspace(0, 2 * np.pi, 50)
    print(a)
    b = np.sin(a)
    print(b)
    plt.plot(a, b)
    mask = b > 0
    print(mask)
    print(a[mask])
    print(b[mask])
    plt.plot(a[mask], b[mask], 'bo')
    mask = (b > 0) & (a <= np.pi / 2)
    print(mask)
    print(a[mask])
    print(b[mask])
    plt.plot(a[mask], b[mask], 'go')
    plt.show()

    a = np.arange(0, 100, 10)
    b = a[:5]
    print(b)
    c = a[a >= 50]
    print(c)
