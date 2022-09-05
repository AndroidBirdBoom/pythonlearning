import numpy
import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = 3
    d = (b - a) / 3
    print(d, type(d), d.shape)

    c = np.array([1, 2, 1])
    x = a < b
    y = c < a
    z = x & y
    z = (a < b) & (c < a)
    print(x, type(x), y, type(y), z)
    print(c[x])

    z = np.where((a < b) & (c < a))
    print(a[z])

    a = np.zeros((5, 4))
    print(a)
    t = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    a[0, 1] = 2
    print(a)
    x = range(0, 2)
    a[x] = t
    print(a)

    b = np.ones((5, 4))
    print(np.hstack((a, b)))
    print(np.c_[a, b] == np.hstack((a, b)))
    print(np.r_[a, b] == np.vstack((a, b)))

    a = np.arange(0, 10, 2)
    b = np.arange(1, 11, 2)
    m = np.meshgrid(a, b)
    print(m, type(m))

    a = np.arange(0, 10).reshape((2, 5))
    print(a)
    # print(np.sum(a, axis=0))

    b = np.arange(0, 10).reshape(2, 5)
    print(a * b)
    print(np.multiply(a, b))

    for i in range(9, 0, -1):
        print(i)

    a = ['ddd', 'dderr', 'gtt']
    for i, e in enumerate(a):
        print('i  = ', i, 'e==', e)

    a = np.array([1, 2, 3]).reshape(-1, 1)
    b = np.array([4, 5, 6]).reshape(-1, 1)
    print(np.concatenate((a, b), axis=0))
