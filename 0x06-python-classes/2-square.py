#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Creates a size validation

        Args:
            size: size of square
        """

        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise NameError("size must be >= 0")

        self.__size = size
