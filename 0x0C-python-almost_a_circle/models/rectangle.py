#!/usr/bin/python3

""" Rectangle
This module creates a class Rectangle.
Corresponds to Tasks 2, 3.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base
       Creates class rectangle

    Attr:
        __widht: with of rectangle
        __height: height of rectagle
        __x: x position
        __y: y position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes attributes

        Args:
            width: width of rectangle
            height: height if rectangle
            x: x position
            y: y position
        """

        super().__init__(id)   # call super() and initializes id

        if type(width) != int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) != int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) != int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) != int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter fir width

        return: width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value: input width
        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height property
        Return:
            height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property
        Args:
            value: input value for height
        """

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter for x

        return: x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x
        Args:
            value: input x
        """

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter for y

        return: y
        """

        return self.__y

    @x.setter
    def y(self, value):
        """Setter for y
        Args:
            value: input y
        """

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ calculates the area of rectangle

        Return: area
        """

        return self.__width * self.__height

    def display(self):
        """prints rectangle in stdout
        """

        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """prints data of rectangle
        return:
            data of rectangle
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__width)
