#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def max_integer(list=[]):
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer([], None)
        self.assertEqual(max_integer([4], 4)
        self.assertEqual(max_integer([1, 2, 3, 4], 1)
        self.assertEqual(max_integer([1, 2, 4, 3], 3)
        self.assertEqual(max_integer([1.0, 2], 2)
        self.assertEqual(max_integer([-1, -2, -3, -4], -1)
        self.assertRaises(TypeError, max_integer, 4)
        self.assertRaises(TypeError, max_integer, ["string", 4, 5, 1]

if __name__== '__main__':
    unittest.main()
