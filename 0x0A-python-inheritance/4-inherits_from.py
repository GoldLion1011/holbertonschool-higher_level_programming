#!/usr/bin/python3
""" Module: 4-inherits_from
object is an instance of a class that inherited directly
or indirectly from the specified class """


def inherits_from(obj, a_class):
    """ determines if obj is an instance of a class inherited
        directly or indirectly from a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
