#!/usr/bin/python3

"""10. Class to JSON
Returns the dictionary description with simple data structure
Corresponds to Task 10.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure

    Args:
        obj: input object
    """
    return obj.__dict__
