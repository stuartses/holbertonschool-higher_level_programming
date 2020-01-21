#!/usr/bin/python3

"""7. Save Object to a file
Save a json file
Corresponds to Task 7.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import json


def save_to_json_file(my_obj, filename):
    """Save object in a JSON file

    Args:
        my_obj: object
        filename: filename
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
