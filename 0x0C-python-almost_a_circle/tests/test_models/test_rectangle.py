#!/usr/bin/python3
""" Unittest Rectangle
    Test cases for Rectangle class """


import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle """
    def test_rect_id(self):
        """ check Rectangle for id """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.id, 12)
        r5 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r5.id, 34)
        r6 = Rectangle(10, 2, 4, 5, -6)
        self.assertEqual(r6.id, -6)
        r7 = Rectangle(10, 2, 4, 5, 8)
        self.assertEqual(r7.id, 8)

    def test_rect_attrs(self):
        """ check Rectangle for attribute values """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_rect_args(self):
        """ checks Rectangle for missing arguments """
        r1 = Rectangle(3)
        self.assertEqual(
            "__init__() missing 1 required positional argument:'height'", str(
                x.exception))
        s = ("__init__() missing 2 required positional" +
             " arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as x:
            r2 = Rectangle
        self.assertEqual(s, str(x.exception))

    def test_rect_inherit(self):
        """ checks Rectangle for inheritance """
        r1 = Rectangle(9, 3)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

if __name__ == '__main__':
    unittest.main()
