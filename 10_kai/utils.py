import numpy as np
from matplotlib import pyplot as plt


def plot_points(x, y, title):
    # plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y)
    # plt.show()


def plot_line(w, b, title):
    # plt.title(title)
    # plt.xlabel('x')
    # plt.ylabel('y')
    x = np.linspace(0, 100, num=100)
    y = w * x + b
    plt.plot(x, y)
    # plt.show()
