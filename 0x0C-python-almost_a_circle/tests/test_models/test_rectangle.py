#!/usr/bin/python3
""" Unittest Rectangle
    Test cases for Rectangle class """


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle """
    def test_rect_init(self):
        """ checks for type """
        with self.assertRaises(ValueError):
            Rectangle(-1, 1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1, 100)
        with self.assertRaises(TypeError):
            Rectangle('1', 1, 0, 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, '1', 0, 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, '0', 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, '0', 100)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, 0, '100')

if __name__ == '__main__':
    unittest.main()
