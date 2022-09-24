#!/usr/bin/python3
""" Unittest Base
    Test cases for Base class """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test class for Base """

    def test_docstring(self):
        """ checks module and function docstrings """
        modDocstring = __import__('models').base.__doc__
        self.assertIsNotNone(modDocstring)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.create.__doc__)

    def test__init__(self):
        """ test initialization of Base class """
        pass

    def test_is_int(self):
        """ creates new instances, checks if id is an integer """
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(11)
        self.assertEqual(b2.id, 11)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(899)
        self.assertEqual(b4.id, 899)
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)
        b6 = Base(6)
        self.assertEqual(b6.id, 6)
        b7 = Base(None)
        self.assertEqual(b7.id, 3)
        self.assertRaises(TypeError, Base, "3")

    def test_is_type(self):
        """ tests for type and instance """
        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(b6, Base)

    def test_to_json_string(self):
        """ something """
        pass

    def test_save_to_file(self):
        """ something else """
        pass

    def test_from_json_string(self):
        """ stuffs """
        pass

    def test_create(self):
        """ stuffs """
        pass

    def test_load_from_file(self):
        """ yeppers """
        pass

if __name__ == '__main__':
    unittest.main()
