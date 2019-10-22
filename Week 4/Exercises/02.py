"""Remove all items from an array with values from 0-9 that are present
in a second array with values from 3-7. Print the result."""
import numpy as np

array = np.arange(10)
remove_array = np.arange(3, 8)
array = np.delete(array, remove_array)
print(array)
