#!/usr/bin/python3

"""1. Number of lines
Count the numbers of lines in a file
Corresponds to Task 1.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def number_of_lines(filename=""):
    """Count the numbers of lines in a input file

    Args:
        filename: input file
    """

    i = 0
    with open(filename, "r") as f:
        for line in f:
            i += 1

    return i
