"""Replace all odd numbers from an array of values from 0-9 with the value -1 and print the result."""
import numpy as np

array = np.arange(0, 10)
array[array % 2 == 1] = -1
print(array)
