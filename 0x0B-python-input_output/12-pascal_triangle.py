#!/usr/bin/python3
""" Module 12-pascal_triangle
    list of lists of integers representing the Pascal’s triangle """


def pascal_triangle(n):
    """ Function that returns a list of lists of integers
        representing the Pascal’s triangle """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(n - 1):
        row = triangle[i]
        temp_1 = row + [0]
        temp_2 = [0] + row
        new_row = []
        for j in range(len(temp_1)):
            new_row.append(temp_1[j] + temp_2[j])
        triangle.append(new_row)

    return triangle
