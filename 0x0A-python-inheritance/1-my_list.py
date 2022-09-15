#!/usr/bin/python3
""" Module: 1-my_list
    Creates class inheriting from list class"""


class MyList(list):
    """ class MyList inherits from list """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))
