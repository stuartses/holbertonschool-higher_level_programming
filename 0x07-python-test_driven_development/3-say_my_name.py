#!/usr/bin/python3


"""2. Say my name
This module prints The input full name
Corresponds to Task 2.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>
    Args:
        first_name (str): First Name
        last_name (str): Last Name
    Returns:
        Prints Full Name
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
