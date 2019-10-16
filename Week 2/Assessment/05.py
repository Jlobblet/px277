"""Write a function called "unique(data1, data2)" which returns the
unique element union of two input arrays data1 and data2."""
import numpy as np


def unique(data1, data2):
    return np.unique(np.concatenate((data1, data2)))
