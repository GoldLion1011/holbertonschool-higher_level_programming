#!/usr/bin/python3
""" Module 8-class_to_json
    Function that returns the dictionary description with simple
    data structure for JSON serialization of an object """


def class_to_json(obj):
    """ returns dict description for JSON serialization"""

    return obj.__dict__
