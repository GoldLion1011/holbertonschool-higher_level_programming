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

    def test_area(self):
        """ checks area """
        r1 = Rectangle(3, 2, 0, 0, 99)
        self.assertEqual(r1.area(), 6)

    def test_display(self):
        """ """
        pass

    def test__str__(self):
        """ checks for str return """
        r1 = Rectangle(3, 2, 0, 0, 99)
        self.assertEqual(str(r1), '[Rectangle] (99) 0/0 - 3/2')

    def test_update(self, *args, **kwargs):
        """ checks for dict updates """
        r1 = Rectangle(3, 2, 0, 0, 99)
        r1.update(100, 4, 3, 1, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 100)
        r1.update(width=5, height=4, x=2, y=2, id=101)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 101)

if __name__ == '__main__':
    unittest.main()
