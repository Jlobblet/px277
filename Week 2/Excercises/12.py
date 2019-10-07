"""Create two arrays from 0-4 as 2 x 2 arrays and stack them vertically to form and print a single 4 x 2 array."""
import numpy as np

array1 = np.arange(5)
array2 = np.arange(5)
array3 = np.column_stack((array1, array2))
print(array3)
