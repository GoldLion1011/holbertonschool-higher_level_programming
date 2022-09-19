#!/usr/bin/python3
""" Module 7-add_item
    Script that adds all arguments to a Python list
    and then save them to a file """


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    my_file = load('add_item.json')

except(TypeError, FileNotFoundError):
    my_file = []

for i in sys.argv[1:]:
    my_file.append(i)

save(my_list, 'add_item.json)
