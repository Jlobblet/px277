"""Integrate the function

I_n,m = ∫-π/2, π/2 sin^n(x)cos^m(x) dx

with parameter values set at n=2 and m=1. Print your result but not the
error output from "quad". Look up how to hand over function parameters
to the integration function "scipy.integrate.quad".
"""
import numpy as np
from scipy.integrate import quad

n = 2
m = 1


def integrand(x, n, m):
    return np.sin(x) ** n * np.cos(x) ** m


print(quad(integrand, -0.5 * np.pi, 0.5 * np.pi, args=(n, m))[0])
