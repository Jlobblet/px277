"""Write a function "stats(data)" which returns the mean, the standard
deviation and the variance of the input numpy array elements data as a
tuple.
"""
import numpy as np


def stats(data):
    return np.mean(data), np.std(data), np.std(data) ** 2
