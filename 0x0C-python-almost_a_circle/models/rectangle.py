#!/usr/bin/python3
""" Module Rectangle
    creates a Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ describes a Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a Rectangle instance """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieves width attribute """

        return self.__width

    @property
    def height(self):
        """ retrieves height attribute """

        return self.__height

    @property
    def x(self):
        """ retrieves x attribute """

        return self.__x

    @property
    def y(self):
        """ retrieves y attribute """

        return self.__y

    @width.setter
    def width(self, value):
        """ sets width attribute """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height attribute """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ sets x attribute """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ sets y attribute """

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns area of the Rectangle """

        return self.__width * self.__height

    def display(self):
        """ displays Rectangle using #'s """

        print('\n' * (self.__y), end="")
        for j in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ returns string representation of Rectangle """

        return (f'[Rectangle] ({self.id})'
                f'{self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')
