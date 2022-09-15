#!/usr/bin/python3
""" Module: 2-is_same_class
Object is an instance of a class """


def is_same_class(obj, a_class):
    """ determines if obj is an exact instance of a_class """
    return True if type(obj) is a_class else False
