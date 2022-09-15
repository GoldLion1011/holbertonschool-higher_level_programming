#!/usr/bin/python3
""" Module: 1-my_list
    Creates class inheriting from list class"""


class MyList(list):
    """ class MyList inherits from list """

    def print_sorted(self):
        """ Prints a list in ascending order """

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
