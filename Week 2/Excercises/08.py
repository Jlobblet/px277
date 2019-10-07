"""Consider the 2D array ((1, 2), (3, 4)). Extract and print the second column values, then print the second row values."""
import numpy as np

array = np.array(((1, 2), (3, 4)))
print(array[:, 1])
print(array[1, :])
