#!/usr/bin/python3
""" Module 3-to_json_string
    function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string) """

    return json.dumps(my_obj)
