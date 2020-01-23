#!/usr/bin/python3

"""13. Student to JSON
Retrieves a dictionary representation of Students
Corresponds to Task 13
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

    def to_json(self, attrs=None):
        """Return dictionary respresentation of names atributes

        Args:
            attrs: list of atributes
        """

        dict_list = self.__dict__
        dict_out = {}

        if attrs is not None:
            if all(type(x) == str for x in attrs):
                for s in attrs:
                    if s in dict_list:
                        dict_out[s] = dict_list[s]

                return dict_out

        return dict_list

    def reload_from_json(self, json):
        """Updates the data of a Student

        Args:
            json: dictionary with new data
        """

        for keys_js in json.keys():
            self.__dict__[keys_js] = json[keys_js]
