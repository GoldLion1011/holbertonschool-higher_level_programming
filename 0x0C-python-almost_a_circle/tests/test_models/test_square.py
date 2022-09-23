#!/usr/bin/python3
""" Unittest Square
    Test cases for Square class """


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test class for Square """
    def test_square_init(self):
        """ checks for type """
        with self.assertRaises(ValueError):
            Square(-1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Square(1, -1, 0, 100)
        with self.assertRaises(ValueError):
            Square(1, 0, -1, 100)
        with self.assertRaises(TypeError):
            Square('1', 0, 0, 100)
        with self.assertRaises(TypeError):
            Square(1, '0', 0, 100)
        with self.assertRaises(TypeError):
            Square(1, 0, '0', 100)
        with self.assertRaises(TypeError):
            Square(1, 0, 0, '100')

if __name__ == '__main__':
    unittest.main()    