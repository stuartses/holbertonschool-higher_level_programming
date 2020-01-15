#!/usr/bin/python3

""" 1. Simple rectangle
This module creates a class Rectangle.
Corresponds to Task 1.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class Rectangle:
    """Class Rectangle
    Creates a new Rectangle

    Attributes:
        __width: width size of the rectangle
        __height: height size of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes attributes

        Args:
            widht: width of rectangle
            height: height of rectangle
        """

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for Width property

        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the property width

        Args:
            value: input value for width
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

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
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
