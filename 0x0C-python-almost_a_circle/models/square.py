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

    def update(self, *args, **kwargs):
        """ assigns value to an unknown number of arguments """

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
