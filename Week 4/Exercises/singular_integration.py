"""The function sinc(x)=sin(πx)/(πx) has a singularity at x=0. The
integration function "quad" can integrate across a singular point in
case it is told about it beforehand. Integrate sinc(x) from
−2≤x≤2 and note that this function is predefined in numpy for
your use.
Print your result but not the error output from scipy.integrate.quad.
"""
from numpy import sinc
from scipy.integrate import quad

print(quad(sinc, -2, 2, points=(0,))[0])
