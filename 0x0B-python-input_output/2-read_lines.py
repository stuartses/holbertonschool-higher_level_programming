#!/usr/bin/python3

"""2. Read n lines
reads n lines of a text file (UTF8) and prints it to stdout
Corresponds to Task 0.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def read_lines(filename="", nb_lines=0):
    """Prints in stdout the first nb_lines of a file

    Args:
        filename: the name of file
        nb_lines: number of lines
    """
    with open(filename, "r") as f:
        i = 0
        for line in f:
            i += 1

            if i > nb_lines and nb_lines > 0:
                break

            print(line, end='')
