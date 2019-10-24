"""Write a function "intersection(data1, data2)" which returns only
the common items between input arrays data1 and data2.
"""
import numpy as np


def intersection(data1, data2):
    return np.intersect1d(data1, data2)
