#!/usr/bin/python3
""" 4. Only sub class of
Check if object is a instance of class that inherited directly or indirectly
Corresponds to Task 4.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: object
        a_class: class

    Return:
        True or False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
