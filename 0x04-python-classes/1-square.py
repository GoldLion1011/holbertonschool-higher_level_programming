#!/usr/bin/python3
"""Info pertaining to square classes"""


class Square:
    """Creates an empty square"""

    def __init__(self, size=0):
        """Initializes square, sets size, checks for size errors"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
