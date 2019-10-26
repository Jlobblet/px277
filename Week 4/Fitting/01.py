"""Use the NumPy "polyfit()" function to fit a parabola to data values.
Create x values from 0-9 and calculate y values using y=x^2+1.2. In
order to avoid perfect data, shift the value stored in "y[2]" by adding
0.1. Then fit using "polyfit()" and print the best fit values.
"""
import numpy as np

x = np.arange(10)
y = x ** 2 + 1.2
y[2] += 0.1

print(np.polyfit(x, y, deg=2))
