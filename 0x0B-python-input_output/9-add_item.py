#!/usr/bin/python3

"""9. Load, add, save
Adds argument to a JSON file
Corresponds to Task 9.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_args = sys.argv[1:]
init_obj = []

# Check if file exists
try:
    init_obj = load_from_json_file(filename)

except IOError:
    with open(filename, "w") as f:
        pass

for x in new_args:
    init_obj.append(x)

save_to_json_file(init_obj, filename)
