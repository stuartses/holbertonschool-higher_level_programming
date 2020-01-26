#!/usr/bin/python3

""" 2. First Rectangle
This module creates a class Rectangle.
Corresponds to Task 2.
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

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter fir width

        return: width
        """

        return self.__wifth

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value: input width
        """

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

        self.__y = value
