#!/usr/bin/python3
""" 2. Exact same object
Check if object is a exact instant of class
Corresponds to Task 2.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instanc
    of the specified class

    Args:
        obj: object
        a_class: class

    Return:
        True or False
    """

    is_type = type(obj) == a_class
    return is_type
