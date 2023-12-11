#!/usr/bin/python3
"""Base class"""


import csv
from distutils.command.config import dump_file
import json

class Base:
    
    """Base class"""
    
    __nb_objects = 0
    def __init__(self, id=None):
        """__init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        """to json tring"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    def save_to_file(cls, list_objs):
        """save_to_file"""

        with open(cls.__name__+".json", encoding="utf-8", mode="w") as file:
            mylist = []
            if list_objs:
                for obj in list_objs:
                    mylist.append(
                        json.loads(cls.to_json_string(obj.to_dictionary())))
            dump_file(mylist, file)
    def from_json_string(json_string):
        """Returns the list of dictionaries from the JSON string representation"""
        if json_string is None or json_string == "":
            return []
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        mycsv = ""
        flag = -1
        for o in list_objs:
            if o.__class__.__name__ == "Rectangle":
                if flag == -1:
                    mycsv += "id,width,height,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.width},{o.height},{o.x},{o.y}\n"

            else:
                if flag == -1:
                    mycsv += "id,size,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.size},{o.x},{o.y}\n"

        with open(cls.__name__+".csv", encoding="utf-8", mode="w") as file:
            file.write(mycsv[:-1])

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        data = []
        with open(cls.__name__+".csv", encoding="utf-8", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert values to integers
                for key in row:
                    row[key] = int(row[key])
                data.append(row)
        return list(map(lambda obj: cls.create(**obj), data))