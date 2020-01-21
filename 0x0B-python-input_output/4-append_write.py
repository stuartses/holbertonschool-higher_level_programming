#!/usr/bin/python3

"""4. Append to a file
Appends in a file
Corresponds to Task 3
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def append_write(filename="", text=""):
    """Appends text in filename

    Args:
        filename: the file
        text: content to write
    """

    with open(filename, "a") as f:
        return f.write(text)
