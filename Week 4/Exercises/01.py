"""Given four position vectors of objects of equal mass, calculate and
print the centre of mass position vector. The position vectors in
form of arrays are: `[0,1,0], [0,0,1], [1,1,0], [1,1,1]`.
"""
import numpy as np

positions = [
    np.array([0, 1, 0]),
    np.array([0, 0, 1]),
    np.array([1, 1, 0]),
    np.array([1, 1, 1]),
]
print(np.mean(positions, axis=0))
