"""Create and print an array with values from 0-9 and negate all elements which are between 3 and 7, in place."""
import numpy as np

array = np.arange(10)
array[(array > 3) & (array <= 7)] = -1 * array[(array > 3) & (array <= 7)]
print(array)
