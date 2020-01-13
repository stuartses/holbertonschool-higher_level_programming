#!/usr/bin/python3


"""3. Print square
This module prints a square
Corresponds to Task 3.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def print_square(size):
    """Function that prints a square of side lenght: size
    Args:
        size (int): Size of side of square

    Returns:
        Prints Square
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        print("#" * size)
