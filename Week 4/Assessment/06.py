"""Calculate the volume of a torus with average radius R and
cross-sectional radius r. The integral to solve is

V = 2∫R-r, R+r 2πxz dx

with

z = √(r^2 - (x - R)^2)

The analytic solution (tedious derivation) to confirm your result is

V = 2π^2Rr^2.

For your numerical calculation you will need to hand over R and r as
parameters to your function. Choose R = 4 and r = 1 for this exercise
and print your result (but not the error output from
scipy.integrate.quad).
"""
import numpy as np
from scipy.integrate import quad

R = 4
r = 1


def integrand(x, R, r):
    z = np.sqrt(r ** 2 - (R - x) ** 2)
    return 4 * np.pi * x * z  # bring the 2 inside the integral


print(quad(integrand, R - r, R + r, args=(R, r))[0])
