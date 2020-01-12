#!/usr/bin/python3

"""0. Integers addition

This module adds two input integer numbers.
Corresponds to Task 0.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry

"""


def add_integer(a, b=98):
    """Functions that adds two integers

    Args:
        a (int): first argument. Could be float, too
        b (int): second argument, by default=98. Could be float, too

    Returns:
        int: The return value convert arguments to integer and adds.

    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
