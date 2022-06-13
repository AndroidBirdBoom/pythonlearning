#!/usr/bin/python
# -*- coding: utf-8 -*-
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

    plt.plot(x, y)
    plt.xlabel('age')
    plt.ylabel('height')
    plt.title('analysis')
    plt.grid(b=True, axis='x', linestyle='--', color='r')
    plt.show()

    xpoints = np.array([0, 6])
    ypoints = np.array([0, 100])
    plt.subplot(2, 2, 1)
    plt.plot(xpoints, ypoints)
    plt.title('plot 1')

    # plot 2:
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])
    plt.subplot(2, 2, 4)
    plt.plot(x, y)
    plt.title('plot 2')

    x1 = np.array([2, 3])
    y1 = np.array([4, 5])
    plt.subplot(2, 2, 2)
    plt.plot(x1, y1)
    plt.title('plot3')
    plt.suptitle('subplot test')
    plt.show()

    x = np.random.randn(3)
    y = np.random.randn(3)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('simple plot')

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('ax1')
    ax2.scatter(x, y)

    fig, (axs, ax1) = plt.subplots(2, 1, subplot_kw=dict(projection='polar'))
    axs.plot(x, y)

    plt.show()
