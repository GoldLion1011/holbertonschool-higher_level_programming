#!/usr/bin/python3
""" Module Square
    creates a class Square which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ describes a Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the Square """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.update(width=value, height=value)

    def __str__(self):
        """ sets string value of Square """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
