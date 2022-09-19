#!/usr/bin/python3
""" Module 2-append_write
    appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
        and returns the number of characters added """

    with open(filename, 'a+') as f:
        return f.write(text)
