"""Create one array with values from 2-9 and print the indices of all elements > 4 and <8."""
import numpy as np

array = np.arange(2, 10)
print(np.where((array > 4) & (array < 8)))
