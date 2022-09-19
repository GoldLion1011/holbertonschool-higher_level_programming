#!/usr/bin/python3
""" Module 6-load_from_json_file
    function that creates an Object from a JSON file """


import json


def load_from_json_file(filename):
    """ Creates an Object from a JSON file """
    with open(filename, 'x') as f:
        return json.load(f)
