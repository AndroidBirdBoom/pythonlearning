#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.markers
import matplotlib.pyplot as plt
import numpy as np


def demo_plot():
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


def pie_demo():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
    plt.scatter(x, y)
    sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90])
    colors = np.array(["red", "green", "black", "orange", "purple", "beige", "cyan", "magenta"])
    plt.scatter(x, y, s=sizes, c=colors)
    plt.show()

    N = 50
    x = np.random.randn(N)
    y = np.random.randn(N)
    # colors = np.random.randn(N)
    colors = np.array(
        [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100, 0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100, 0, 10,
         20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100, 0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 100])
    area = (30 * np.random.rand(N)) ** 2
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='CMRmap')
    plt.colorbar()
    plt.title("scatter title")
    plt.show()

    x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    y = np.array([12, 22, 6, 18])
    colors = np.array(['r', 'b', 'g', 'c'])
    plt.bar(x, y, color=colors, width=0.5, align='center')
    plt.show()

    y = np.array([35, 25, 25, 15])
    plt.pie(y, labels=['A', 'B', 'C', 'D'], colors=['r', 'g', 'b', 'c'], explode=[0, 0.2, 0, 0], autopct='%.1f%%')
    plt.title('pie title')
    plt.show()


if __name__ == "__main__":
    delta = 0.5
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = X - Y
    plt.contour(X, Y, Z)
    plt.show()


    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 生成网格
    X, Y = np.meshgrid(x, y)

    # contour 仅仅绘制出等高线
    C = plt.contour(X, Y, f(X, Y), 8, cmap='hot', linewidth=.5)

    # 添加数据标签
    plt.clabel(C, inline=True, fontsize=10)

    plt.xticks(())
    plt.yticks(())

    plt.show()

