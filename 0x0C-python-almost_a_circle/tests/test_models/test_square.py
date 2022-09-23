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

    def test_to_dictionary(self):
        """ checks dictionary representation and type """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        test_dict = {'id': 6, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dictionary, test_dict)
        self.assertEqual(type(s1_dictionary), dict)

    def test__str__(self):
        """ checks for str return """
        s1 = Square(10, 2, 1, 99)
        self.assertEqual(str(s1), '[Square] (99) 2/1 - 10')

    def test_update(self, *args, **kwargs):
        """ checks for dict updates """
        s1 = Square(10, 2, 1, 99)
        s1.update(100, 1, 10, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 100)
        s1.update(size=2, x=11, y=3, id=101)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 11)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 101)

if __name__ == '__main__':
    unittest.main()
