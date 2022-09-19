#!/usr/bin/python3
""" Module 9-student
    Creates a class Student """


class Student():
    """ defining student attributes """

    def __init__(first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
