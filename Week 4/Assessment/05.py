"""Write a function called "vectorVolume(v1, v2, v3)" that calculates
and returns the volume of a parallelepiped created by three vectors
(v1, v2 and v3 in 2D or 3D). Use the formula V = |a · (b × c)| for
three numpy arrays, a, b and c.
"""
import numpy as np


def vectorVolume(v1, v2, v3):
    return np.absolute(np.dot(v1, np.cross(v2, v3)))
