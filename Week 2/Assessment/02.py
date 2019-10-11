"""Create and print the cumulative sum as an array from a number array with values from 0-5."""
import numpy as np

array = np.arange(6)
print(np.array([sum(array[: place + 1]) for place in range(len(array))]))
