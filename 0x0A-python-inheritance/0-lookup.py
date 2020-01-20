#!/usr/bin/python3

""" 0. Lookup
List of available attributes and methods of an object.
Corresponds to Task 0.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def lookup(obj):
    """Return the list of attributes and method of an object

    Args:
        obj: input object
    """

    return dir(obj)
