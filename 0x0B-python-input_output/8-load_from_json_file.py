#!/usr/bin/python3

"""8. Create object from a JSON file
Get object fromn a JSON file
Corresponds to Task 8.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


import json


def load_from_json_file(filename):
    """Creates a object from a Json file

    Args:
        filename: name of the file
    """

    with open(filename, "r") as f:
        json_line = f.read()

        return json.loads(json_line)
