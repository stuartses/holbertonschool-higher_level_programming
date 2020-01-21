#!/usr/bin/python3
"""0. Read file
Prints the contet of file in stdout
Corresponds to Task 0.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def read_file(filename=""):
    """Prints the content of a filename in stdout
    Args:
        filename: file to read
    """

    f = open(filename, 'r')
    print(f.read())
    f.close()
