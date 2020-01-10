#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Area Of Square

        Args:
            size: size of square
            position: coordinades of square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get coordinades of Square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set coordinades

        Args:
            value: tuple of coordinades
        """

        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the Square with hash # """

        if self.size == 0:
            print()
        else:
            tupla = self.position
            if tupla[1] == 1:
                print()
            if tupla[1] > 1:
                print(" " * tupla[1])

            for y in range(self.__size):
                if tupla[0] > 0:
                    print(" " * tupla[0], end='')
                for x in range(self.__size):
                    print("#", end='')
                print()
