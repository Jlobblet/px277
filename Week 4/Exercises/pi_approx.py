"""(a) Given a NumPy array of N points in 2D, (xi,yi), as input, write
a function to calculate the pathlength defined as the sum of point
differences

L=∑i=1,N√((x_i−x_(i−1))^2+(y_i−y_(i−1))^2).

(b) Use your pathlength function to approximate the calculation of π
by a polygon through N+1 points on a closed circle with radius 1/2.

Write hence a function "pi_approx()" that takes as a single input
parameter the number of point N and creates N+1 points along the closed
circle according to

x=1/2 cos(2πi/N); y=1/2 sin(2πi/N)

with i=0,...,N. Return the approximate value of π.
"""
import numpy as np


def calculate_pathlength(array):
    return sum(
        [
            (
                (array[i][0] - array[i - 1][0]) ** 2
                + (array[i][1] - array[i - 1][1]) ** 2
            )
            ** 0.5
            for i in range(1, len(array))
        ]
    )


def pi_approx(N):
    seq = np.arange(N + 1).T
    x_seq = 0.5 * np.cos(2 * np.pi * seq / N)
    y_seq = 0.5 * np.sin(2 * np.pi * seq / N)
    approx_circle = np.vstack((x_seq, y_seq)).T
    return calculate_pathlength(approx_circle)
