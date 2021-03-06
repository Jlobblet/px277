"""Consider a 4x4 array (values 0-15). Swap the rows 1 and 2 of that array and print the result."""
import numpy as np

array = np.arange(16).reshape((4, 4))
array[[1, 2]] = array[[2, 1]]
print(array)
