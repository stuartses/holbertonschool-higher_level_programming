#!/usr/bin/python3

""" Rectangle
This module creates a class Rectangle.
Corresponds to Tasks 2-9.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base
       Creates class rectangle

    Attr:
        __widht: with of rectangle
        __height: height of rectagle
        __x: x position
        __y: y position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes attributes

        Args:
            width: width of rectangle
            height: height if rectangle
            x: x position
            y: y position
        """

        super().__init__(id)   # call super() and initializes id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width

        return: width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

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

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter for x

        return: x
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x
        Args:
            value: input x
        """

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter for y

        return: y
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y
        Args:
            value: input y
        """

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ calculates the area of rectangle

        Return: area
        """

        return self.__width * self.__height

    def display(self):
        """prints rectangle in stdout
        at the position x, y
        """

        print("\n" * self.__y, end='')  # y offset

        for i in range(self.__height):
            print(" " * self.__x, end='')  # x offset
            print("#" * self.__width)

    def __str__(self):
        """prints data of rectangle
        return:
            data of rectangle
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update rectangle data grom *args arguments

        Args:
            *args: list or argument ordered: id, widht, height, x, y
            **kwargs: list of key/word arguments
        """

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """dictionary representation"""

        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y

        return rect_dict
