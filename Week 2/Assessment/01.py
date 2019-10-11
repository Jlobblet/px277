"""Extract and print all odd numbers from an array of values 0-9."""
import numpy as np

array = np.arange(10)
print(array[array % 2 == 1])
