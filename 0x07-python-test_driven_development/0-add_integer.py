#!/usr/bin/python3
"""
Module: add-integer
Adds two integers to find the sum

"""


def add_integer(a, b=98):
    """Returns the sum of two integers a and b,
       returns an error if a and b are not ints or floats"""

    if type(a) is not int or float:
        raise TypeError('a must be an integer')
    if type(b) is not int or float:
        raise TypeError('b must be an integer')

    if type(a) is float:
        type(a) = a
    if type(b) is float:
        type(b) = b

    return a + b
