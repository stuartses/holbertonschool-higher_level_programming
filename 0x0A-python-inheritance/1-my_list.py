#!/usr/bin/python3

"""1. My list
This module that inherits from list.
Corresponds to Task 1.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class MyList(list):

    def print_sorted(self):
        """prints the list sorted"""

        self.sort()
        print(self)
