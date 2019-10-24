"""Generate a mesh grid of 3x3 values between -1 and 1 and compute and
print 2D normalised Gaussian (2D Normal distribution, μ=0;σ=1) values
on that grid.
"""
import numpy as np

mesh = np.mgrid[-1:2, -1:2]
gaussian = np.exp(-1 * ((mesh[0] ** 2 / 2) + (mesh[1] ** 2 / 2))) * 5 / (4 * np.pi)
print(gaussian)
