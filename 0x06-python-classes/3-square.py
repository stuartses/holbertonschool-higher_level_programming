#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Creates validation of the square size

        Args:
            size: size of square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the Area of a Squeare"""

        return self.__size * self.__size
