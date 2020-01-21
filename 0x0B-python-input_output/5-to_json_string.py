#!/usr/bin/python3

"""5. To JSON string
JSON representation
Corresponds to Task 0.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import json


def to_json_string(my_obj):
    """Return de JSON representation of my_obj

    Args:
        my_obj: input object
    """

    return json.dumps(my_obj)
