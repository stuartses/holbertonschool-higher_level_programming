#!/usr/bin/python3
"""8. Rectangle
Rectangle that inherits from BaseGeometry
Corresponds to Task 8.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle
    Creates a new Rectangle
    Attributes:
        __width: width size of the rectangle
        __height: height size of the rectangle
    """

    def __init__(self, width, height):
        """Initializes attributes
        Args:
            widht: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
