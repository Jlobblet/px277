"""Write a function "normlist()" which normalises a python list, where
normalisation here means normalise all list elements to the biggest
difference of values so that all entries are elements of the interval
"[0,1]". Return the normed list from your function.
Example: say you have a list [1,2,3,4] then the normalisation means the
biggest element difference is 4-1=3 and normalised elements are
calculated as (list element -minimum list member)/3. That results in
list elements in the interval [0-1].
"""


def normlist(array):
    return [(x - min(array)) / (max(array) - min(array)) for x in array]
