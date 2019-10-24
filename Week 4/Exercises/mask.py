"""Create and print a boolean array, a mask, from a NumPy number array
with values from 0-5 and the condition: values ≥ 3.
"""
import numpy as np

array = np.arange(6)
print(array >= 3)
