#!/usr/bin/python3

"""2. Area and Perimeter
This module that calculates area and perimeter of a rectangle.
Corresponds to Task 2.
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

    def area(self):
        """Calculates the area of a rectangle

        Return:
            Area of rectangle Width * Height
        """

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of s rectangle

        Return:
            Perimeter of rectangle 2 * (Width + Height)
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
