#!/usr/bin/python3

""" Square
This module creates a class Square.
Corresponds to Tasks 10.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectangle

    Attr:
        __size: size of square
        __x: x position
        __y: y oposition
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializes arguments

        Args:
            size: size of square
            x: position x
            y: position y
            id: id
        """

        super().__init__(size, size, x, y)
        self.size = size

    def __str__(self):
        """prints data of square
        return:
            data of square
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        """getter for size

        return: size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value

    def update(self, *args, **kwargs):
        """ Update rectangle data grom *args arguments
        Args:
            *args: list or argument ordered: id, size, x, y
            **kwargs: list of key/word arguments
        """

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """dictionary representation"""

        sque_dict = {}
        sque_dict['id'] = self.id
        sque_dict['size'] = self.__size
        sque_dict['x'] = self.x
        sque_dict['y'] = self.y

        return sque_dict
