"""Recycle the data production again and use the "polydeg2()" function
again but here allow for error bars on the y-axis values. For that,
produce an array of values with the same length as x and y and fill it
with the error value 0.55. That would correspond to the ± error bar on
each y value. Use the option "sigma=" in the "curve_fit()" function to
hand over the error array so that the fit function can use it. Print the
(0,0) entry of the covariance matrix which should be slightly larger
than before on the previous exercises. The best fit value should not
have changed.
"""
import numpy as np
from scipy.optimize import curve_fit

x = np.arange(10)
# y = 1.2 x^2
y = x ** 2 + 1.2
y[2] += 0.1
sigma = 0.55 * np.ones(len(x))


def polydeg2(x, a, b, c):
    return a * x ** 2 + b * x + c


print(curve_fit(polydeg2, x, y, sigma=sigma)[1][0, 0])
