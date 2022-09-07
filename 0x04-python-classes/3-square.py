#!/usr/bin/python3
"""Info pertaining to square classes"""


class Square:
    """Creates an empty square"""

    def __init__(self, size=0):
        """Initializes square, sets size and checks for errors"""
        self.__size = size

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
