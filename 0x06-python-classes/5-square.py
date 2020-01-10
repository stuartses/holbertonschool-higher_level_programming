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
        """Settter for the value of size

        Args:
            value: size of square
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates Area Square """

        return self.__size * self.__size

    def my_print(self):
        """Prints the Square with hash # """

        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
