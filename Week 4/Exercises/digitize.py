"""Look up and use "np.digitize()" to print the index position of the
bin each element belongs to for the array with values from 0-9 and bins
(0, 3, 6, 9).
"""
import numpy as np

bins = (0, 3, 6, 9)
array = np.arange(10)
print(np.digitize(array, bins))
