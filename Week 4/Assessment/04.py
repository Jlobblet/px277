"""Find and print all the peak positions in a 1D numpy array Z. Peaks
are points surrounded by smaller values on both sides. Let Z consist of
the values (1, 3, 7, 1, 2, 6, 0, 1). A short solution uses "np.diff()".
Print your peak indices in form of a numpy array.
"""
import numpy as np

Z = np.array((1, 3, 7, 1, 2, 6, 0, 1))
Z_diff = np.diff(Z)
adj = [np.array((Z_diff[i], Z_diff[i + 1])) for i in range(len(Z_diff) - 1)]
maxima = np.array([i + 1 for i in range(len(adj))
                   if adj[i][0] >= 0 and adj[i][1] < 0])
print(maxima)
