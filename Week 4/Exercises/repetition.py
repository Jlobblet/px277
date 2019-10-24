"""Find and print the index of the 5th repetition of the number 1 in an
array with values (1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2).
"""
import numpy as np

array = np.array((1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2))
count_ones = np.array(array == 1, dtype=int)
for i in range(len(count_ones)):
    if sum(count_ones[: i + 1]) == 5:
        print(i)
        break
