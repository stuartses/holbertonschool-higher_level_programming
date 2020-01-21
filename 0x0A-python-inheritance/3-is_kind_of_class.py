#!/usr/bin/python3
""" 3. Same class or inherit from
Check if object is a instance of class
Corresponds to Task 3.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: object
        a_class: class

    Return:
        True or False
    """

    return isinstance(obj, a_class)
