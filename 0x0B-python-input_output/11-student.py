#!/usr/bin/python3
""" Module 9-student
    Creates a class Student """


class Student:
    """ defining Student attributes """

    def __init__(self, first_name, last_name, age):
        """ initializes the Student instance """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of Student instance """

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """

        for x in json:
            self.__dict__.update({x: json[x]})
