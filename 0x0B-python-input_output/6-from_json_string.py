#!/usr/bin/python3

"""6. From JSON string to Object
Dedoce JSON to object
Corresponds to Task 6.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import json


def from_json_string(my_str):
    """Decodes JSON string to Object

    Args:
        my_str: json input
    """

    return json.loads(my_str)
