"""Copy the data production from the previous exercise, x values and y
values, the parabola with shifted "y[2]" value. Then write a function
"polydeg2(x, a, b, c)" which calculates and returns a general parabola
according to y(x)=ax^2+bx+c. Finally, use the SciPy function
"curve_fit()" to fit the parabola in "polydeg2()" to the data and print
the best fit values. They should be identical to the NumPy fit with
"polyfit()". The fit uncertainties will be different though if you were
to print the covariance matrices (and fail the trivial Coderunner tests
since that is not expected).
"""
import numpy as np
from scipy.optimize import curve_fit

x = np.arange(10)
# y = 1.2 x^2
y = x ** 2 + 1.2
y[2] += 0.1


def polydeg2(x, a, b, c):
    return a * x ** 2 + b * x + c


print(curve_fit(polydeg2, x, y)[0])
