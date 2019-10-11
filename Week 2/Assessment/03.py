"""Write a function called "max_minus_min(x)" which takes a 1D numpy
array as input and calculates the difference between the maximum
value in x and the minimum value in x and returns the result."""
import numpy as np


def max_minus_min(x):
    return max(x) - min(x)
