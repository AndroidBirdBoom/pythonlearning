import numpy as np
from numpy import *
import matplotlib.pyplot as plt


def demo_numpy1():
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

    a = np.arange(0, 100, 10)
    b = np.where(a < 50)
    c = np.where(a >= 50)[0]
    print(b, type(b))
    print(c, type(c))

    s = {'fish', 'mouse'}
    print(s)
    s.add('fish')
    print(s)

    d = {(x, x + 1): x for x in range(10)}
    print(d)


if __name__ == "__main__":
    az = np.array([[11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25],
                   [26, 27, 28, 29, 30],
                   [31, 32, 33, 34, 35]])

    print(az[1, 2])

    a = np.zeros((2, 4))
    print(a)

    b = np.ones((1, 2))
    print(b)

    c = np.full((2, 2), 3)
    print(c)

    d = np.eye(3)
    print(d)

    e = np.random.random((2, 4))
    print(e)

    a = np.arange(1, 13)
    print(a)
    a = a.reshape((3, 4))
    print(a)
    b = a[:2, 1:3]
    print(b)
    b[1, 1] = 100
    print(b)
    print(a)

    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a, type(a))
    indic = [0, 1]
    print(a[[0, 1, 2], [0, 1, 0]])
    print(a[indic])

    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

    b = np.array([0, 2, 0, 1])

    c = a[np.arange(4), b]
    print(c)
    c += 10
    print(c, a)
    a[range(4), b] += 10
    print(a)

    b = a > 5
    print(b)
    print(a[b])
    print(a[a > 5])

    x = np.array([1, 2])
    print(x.dtype)
    x = np.array([1., 2.])
    print(x.dtype)
    x = np.array([1, 2], dtype=np.int64)
    print(x.dtype)

    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)
    print(x)
    print(y)

    print(x + y)

    print(np.add(x, y))

    print(x - y)
    print(np.subtract(x, y))

    print(x * y)
    print(np.multiply(x, y))

    print(x / y)
    print(np.divide(x, y))

    print(x, np.sqrt(x))

    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    v = np.array([9, 10])
    w = np.array([11, 12])

    print(v.dot(x))
    print(np.dot(v, x))

    print(x.dot(v))
    print(np.dot(x, v))

    x = np.array([[1, 2], [3, 4]])
    print(np.sum(x))
    print(np.sum(x, axis=0))
    print(np.sum(x, axis=1))

    print(x)
    print(x.T)
    print(np.sum(x.T, axis=0))

    v = np.array([1, 2, 3])
    print(v, v.shape)
    print(v.T, v.T.shape)

    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])

    y = np.empty_like(x)
    print(y)
    y[1, :] = [4, 4, 4]
    print(y)
    for i in range(4):
        y[i, :] = x[i, :] + v
    print(y)

    vv = np.tile(v, (4, 1))
    print(vv)
    print(vv + x)
    print(v + x)

    v = np.array([1, 2, 3])  # v has shape (3,)
    w = np.array([4, 5])  # w has shape (2,)
    print(v.shape)
    print(np.reshape(v, (3, 1)) * w.reshape((1, 2)))
    # v = np.reshape(v, (3, 1))
    # print(v.shape)

    x = np.array([[1, 2, 3], [4, 5, 6]])
    print(x.shape)
    print(v.shape)
    print(x.dot(v.reshape((3, 1))))

    print(x + v)
    # print(x.T + w.reshape((1, 2)))
    print(x + w.reshape(2, 1))

    a = np.arange(8).reshape(2, 2, 2)
    b = np.arange(2).reshape(1, 2, 1)
    print(a)
    print(b)

    a = np.array([[[0],
                   [10],
                   [20],
                   [30]]])
    b = np.array([[[1, 2, 3, 4, 5]],
                  [[1, 2, 3, 4, 5]],
                  [[1, 2, 3, 4, 5]],
                  [[1, 2, 3, 4, 5]]])

    print(a.shape, b.shape)
    # print(a.reshape((4, 1, 1)))
    print(a.reshape((4, 1, 1)) + b)
