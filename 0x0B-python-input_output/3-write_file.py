#!/usr/bin/python3

"""3. Write to a file
Writes in a file
Corresponds to Task 3
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


def write_file(filename="", text=""):
    """Writes text in filename

    Args:
        filename: the file
        text: content to write
    """

    with open(filename, "w") as f:
        return f.write(text)
