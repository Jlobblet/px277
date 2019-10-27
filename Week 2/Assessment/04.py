"""Write a function called "increasing(data)" that prints True if the
input array is increasing or False otherwise. Hint: np.diff() returns
the difference between consecutive elements of a sequence.
"""
import numpy as np


def increasing(data):
    """Take an array and return whether the array is strictly increasing or not.

    Parameters:
    ------
    data: numpy array to be tested
    Returns:
    ------
    Bool whether the array is strictly increasing or not.
    """
    return (np.diff(data) > 0).all() == True
