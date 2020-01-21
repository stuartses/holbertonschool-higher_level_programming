#!/usr/bin/python3
"""9. Full rectangle
Implements Area and _str_
Corresponds to Task 9.
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

    def area(self):
        """Calculates the area of a rectangle
        Return:
            Area of rectangle Width * Height
        """

        return self.__width * self.__height

    def __str__(self):
        """Prints rectangle description: [Rectangle] <width>/<height>

        Return: string
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
