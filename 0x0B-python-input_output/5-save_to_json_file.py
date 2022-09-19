#!/usr/bin/python3
""" Module 5-save_to_json_file
    function that writes an Object to a text file,
    using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to text file using a JSON representation"""

    with open(filename, 'w+') as f:
        return json.dumps(my_obj)
