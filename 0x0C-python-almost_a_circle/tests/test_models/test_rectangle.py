#!/usr/bin/python3
""" Unittest Rectangle
    Test cases for Rectangle class """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test class for Rectangle """
    def test_is_rect(self):
        """ creates new instances, checks that id is an integer"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 2)

















if __name__ == '__main__':
    unittest.main()    
