#!/usr/bin/python3
""" Module: 3-is_kind_of_class
Finds if object is an instance of or inherited from an
instance of a class """


def is_kind_of_class(obj, a_class):
    """ Finds if obj is an instance of or inherited from a_class """
    return isinstance(obj, a_class)
