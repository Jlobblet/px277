"""Same again as before, recycle the data production and parabola
function. Also recycle your uncertainty array. Now create a tuple
containing upper and lower bounds for the fit parameters in the form of
arrays (or lists), i.e. a tuple such as "([0,0,0], [10.0, 0.1, 1.1])"
would mean all parameter lower bounds at zero, parameter "a" upper bound
is 10.0, parameter "b" upper bound at 0.1 and "c" upper bound is 1.1
(note: lower than the current best fit and true value of 1.2).
Fit the parabola using "curve_fit" with the data as before but now set
the option "bounds=" to your boundary tuple and see how that affects the
fit result. Print the best fit (and the covariance matrix, even if not
tested in Coderunner).
"""
import numpy as np
from scipy.optimize import curve_fit

x = np.arange(10)
# y = 1.2 x^2
y = x ** 2 + 1.2
y[2] += 0.1
sigma = 0.55 * np.ones(len(x))
bounds = ([0, 0, 0], [10, 0.1, 1.1])


def polydeg2(x, a, b, c):
    return a * x ** 2 + b * x + c


print(curve_fit(polydeg2, x, y, sigma=sigma, bounds=bounds)[0])
