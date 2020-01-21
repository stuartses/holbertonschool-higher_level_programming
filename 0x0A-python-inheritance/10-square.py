#!/usr/bin/python3
"""9. Full rectangle
Inherits from Rectangle in Task 9
Corresponds to Task 10.
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
