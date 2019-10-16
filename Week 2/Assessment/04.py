"""Write a function called "increasing(data)" that prints True if the
input array is increasing or False otherwise. Hint: np.diff() returns
the difference between consecutive elements of a sequence."""
import numpy as np


def increasing(data):
    return (np.diff(data) > 0).all() == True
