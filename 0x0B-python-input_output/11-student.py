#!/usr/bin/python3

"""11. Student to JSON
Retrieves a dictionary representation of Students
Corresponds to Task 11.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""


class Student:
    """Class Student
    Creates a new Student
    Attributes:
        first_name: First name of student
        last_name: Last name of student
        age: age of student
    """

    def __init__(self, first_name, last_name, age):
        """Initializes attributes
        Args:
            first_name: First name of student
            last_name: Last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary respresentation """

        return self.__dict__
