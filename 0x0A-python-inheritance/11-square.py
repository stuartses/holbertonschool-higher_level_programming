#!/usr/bin/python3
"""11. Square #2
Inherits from Rectangle in Task 9 and implementa own _str_
Corresponds to Task 11.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square
    Creates a new Square
    Attributes:
        __size: size of the Square
    """

    def __init__(self, size):
        """Initializes attributes
        Args:
            size: size of Square
        """

        self.__size = size
        self.integer_validator("size", self.__size)

        # initializes rectangle with size as width and height
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Prints square description: [Square] <width>/<height>
        Return: string
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
