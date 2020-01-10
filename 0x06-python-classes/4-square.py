#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initializes Area Of Square

        Args:
            size: size of sqare
        """

        self.__size = size

    @property
    def size(self):
        """Getter for size of square

        Return:
            The size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size

        Args:
            value: size of square
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
