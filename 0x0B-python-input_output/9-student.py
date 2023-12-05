#!/usr/bin/python3
"""student to json"""

class_to_json = __import__('8-class_to_json').class_to_json

class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return class_to_json(self)