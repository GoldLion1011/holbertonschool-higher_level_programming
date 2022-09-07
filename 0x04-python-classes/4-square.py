#!/usr/bin/python3
"""Info pertaining to square classes"""


class Square:
    """Creats an empty square"""

    def __init___(self, size=0):
        """Intializes square"""
        self.__size = size

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(size, value):
        """Sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print(self.__size 8 "#", end="")
            print()
