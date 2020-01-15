#!/usr/bin/python3

"""6. How many instances
This module calculates area and perimeter of a rectangle.
And counts instances

Corresponds to Task 6.
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

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes attributes

        Args:
            widht: width of rectangle
            height: height of rectangle
        """

        if type(width) != int:
            raise TypeError("width must be an integer")

        if type(height) != int:
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """Prints the rectangle with Hash using method "str"

        Return:
            string with rectangle
        """

        str_x = ""
        for x in range(self.__height):
            str_x += "#" * self.__width

            if x < self.__height - 1:
                str_x += "\n"

        return str_x

    def __repr__(self):
        """Reproduce object Rectangle

        Return:
            Rectangle()
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instence """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
