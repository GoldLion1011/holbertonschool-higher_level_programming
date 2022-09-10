#!/usr/bin/python3
"""
Module: matrix_divided
Divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """Divides every element of a matrix of equal rows
       rounded to 2 decimal places"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')

    for row in matrix:
        if len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            'of integers/floats')
        for z in row:
            if type(z) is not int and type(z) is not float:
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))

    if not all(elem == len(rows)[0] for elem in len(rows):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda x : round(x / div, 2), row)) for row in matrix])
