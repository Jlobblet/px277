"""Create a numpy array with integer values from 0 to 9. Using that, print another array of the same length containing 0 at the position of even numbers and 1 at the position of odd numbers."""
import numpy as np

array1 = np.arange(10)
array2 = np.where(array1 % 2 == 0, 0, 1)
print(array2)
