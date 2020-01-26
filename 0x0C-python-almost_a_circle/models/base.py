#!/usr/bin/python3

"""1. Base class
Creates the Base Class
Corresponds to Task 1.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class Base:
    """Class Base
    Base Class for project

    Attributes:
        __nb_objects: counter of new objects
        id: id of object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes attributes

        Args:
            id: id of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects