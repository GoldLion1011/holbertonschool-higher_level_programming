#!/usr/bin/python3
""" Unittest Base
    Test cases for Base class,
    ordered by test_task_testnumber """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class for Base """

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

        if __name__ == '__main__':
            unittest.main()
