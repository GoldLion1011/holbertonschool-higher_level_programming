#!/usr/bin/python3
""" Module base
    defines Base class for other classes in this project """


class Base:
    """ class with private attribute
        __nb_objects """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization of a Base instance """

        if type(id) != int and id is not None:
            raise TypeError('id must be an integer')
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
