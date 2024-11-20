import matplotlib.pyplot as plt
import numpy as np

from scipy import integrate
from math import exp, sqrt, pi


@np.vectorize
def func(x, y, t):
    return exp(
        -t * (3 * x**2 + 3 * y**2 - 2 * x * y - 16 * sqrt(2) * x - 8 * sqrt(2) * y + 76)
    ) / (sqrt(x**2 + 3 / 2) * sqrt(y**2) + 1 / 2)


@np.vectorize
def approx(t):
    return pi / (52 * t)


@np.vectorize
def calc(t):
    return integrate.dblquad(func, -16, 16, -16, 16, args=(t,))[0]


t = np.arange(0.01, 0.2, 0.01)
calc_result = calc(t)
approx_result = approx(t)

plt.plot(t, calc_result, label="F(t)")
plt.plot(t, approx_result, label="approx F(t)")
plt.xlabel("t")
plt.ylabel("F(t)")
plt.legend(loc="best")
plt.show()
