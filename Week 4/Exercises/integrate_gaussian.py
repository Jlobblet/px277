"""Integrate the function f(x)=exp(−x^2) from 0 to ∞ using the
scipy function "scipy.integrate.quad()". Note that you can use special
numpy expressions such as "np.inf".
Print your result but not the error output from quad.
"""
from scipy.integrate import quad
import numpy as np


def gaussian(x):
    return np.exp(-x ** 2)


print(quad(gaussian, 0, np.inf)[0])
