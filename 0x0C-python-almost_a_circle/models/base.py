#!/usr/bin/python3
"""base class module"""

from json import dump
from json import dumps
from json import loads
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init
        args:
            id : int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
         returns the JSON string representation
         args:
            list_dictionaries
        return:
             JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        """
        if list_objs is None:
            list_objs = "[]"
        filename = f"{cls.__name__}.json"
        j_list = [obj.to_dictionary() for obj in obj_list]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(j_list))

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """craete an instance"""
        from models.rectangle import Rectangle
        from models.square import Square
        instance = None
        if cls.__name__ == "Rectangle":
            instance = Rectangle(1, 1)
        else:
            instance = Square(1)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """lode json from file"""
        try:
            with open(cls.__name__+".json", encoding="utf-8",
                      mode="r") as file:
                content = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return list(map(lambda obj: cls.create(**obj), content))
