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

    def test_to_dictionary(self):
        """ checks dictionary representation and type """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        test_dict = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1_dictionary, test_dict)
        self.assertEqual(type(r1_dictionary), dict)

if __name__ == '__main__':
    unittest.main()
