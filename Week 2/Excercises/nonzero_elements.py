"""Find and print indices of non-zero elements from the NumPy array [1,2,0,0,4,0]."""
import numpy as np

array = np.array([1, 2, 0, 0, 4, 0])
print(np.where(array != 0)[0])
