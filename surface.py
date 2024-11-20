import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from math import exp, sqrt


@np.vectorize
def func(x, y, t):
    return exp(
        -t * (3 * x**2 + 3 * y**2 - 2 * x * y - 16 * sqrt(2) * x - 8 * sqrt(2) * y + 76)
    ) / (sqrt(x**2 + 3 / 2) * sqrt(y**2) + 1 / 2)


def plot(t):
    x = np.arange(-2, 8, 0.01)
    y = np.arange(-2, 8, 0.01)
    x, y = np.meshgrid(x, y)
    z = func(x, y, t)

    _, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.plot_surface(x, y, z, cmap=cm.coolwarm)
    plt.show()


plot(0.1)
plot(1)
plot(10)
