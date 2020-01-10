#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Area Of Square

        Args:
            size: size of square
            position: coordinades of square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def my_print(self):
        """Prints the Square with hash # """

        if self.__size == 0:
            print()
        else:
            tupla = self.__position
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
