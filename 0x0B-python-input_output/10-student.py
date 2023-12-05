#!/usr/bin/python3
"""student to json"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def to_json(self, attrs=None):
        """that retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            return  {key: value for key, value in self.__dict__.items() if key in attrs}