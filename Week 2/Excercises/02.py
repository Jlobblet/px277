"""Create and print a 4x4 NumPy array with value 1 on the borders and value 0 inside."""
import numpy as np

array = np.ones([4, 4], dtype=int)
array[1:-1, 1:-1] = 0
print(array)
