import matplotlib.markers
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    xpoints = np.array([0, 6, 10])
    ypoints = np.array([0, 20, 100])
    plt.plot(xpoints, ypoints, 'y')
    plt.show()

    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.show()

    ypoints = np.array([1, 3, 4, 5, 8, 9, 6, 1, 3, 4, 5, 2, 4])
    plt.plot(ypoints, marker=matplotlib.markers.CARETUP)
    plt.show()

    plt.plot(ypoints, 'o-.r', ms=13, mfc='c', mec='k')
    plt.plot(xpoints, '8:')
    plt.show()

    x = np.array([0, 4, 10])
    y = np.array([7, 9, 10])
    plt.plot(x, y, marker='o', linestyle=':', color='g', markersize='13', markerfacecolor='c', markeredgecolor='k',
             linewidth=3)
    plt.show()

    plt.plot(x, y, color='g', linestyle='-.', linewidth=1, marker='o')
    plt.show()
