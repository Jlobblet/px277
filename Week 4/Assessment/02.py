"""Compute and print the euclidean distance between two arrays. The
first array shall consist of 5 values from 1-5 and the second array
should have 5 values from 4-8. Check the "numpy.linalg" library for a
suitable function.
"""
import numpy as np

array_1 = np.arange(1, 6)
array_2 = np.arange(4, 9)
print(np.linalg.norm(array_1 - array_2))
