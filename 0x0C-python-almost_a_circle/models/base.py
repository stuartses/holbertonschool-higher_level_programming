#!/usr/bin/python3

"""1. Base class
Creates the Base Class
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import json


class Base:
    """Class Base
    Base Class for project

    Attributes:
        __nb_objects: counter of new objects
        id: id of object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes attributes

        Args:
            id: id of object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return json representation

        Args:
           list_dictionaries: input dictionary
        """

        dict_json = "[]"

        if list_dictionaries is not None:
            dict_json = json.dumps(list_dictionaries)

        return dict_json

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objects in json file

        Args:
            cls:
            list_objs: input object
        """

        filename = cls.__name__ + ".json"
        dict_list = []

        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        json_objs = cls.to_json_string(dict_list)

        with open(filename, "w") as f:
            f.write(json_objs)

    def from_json_string(json_string):
        """return dictionary from json string

        Args:
            json_string: input json
        Return:
            Dictionay
        """

        dict_obj = []
        if json_string is not None:
            dict_obj = json.loads(json_string)

        return dict_obj
