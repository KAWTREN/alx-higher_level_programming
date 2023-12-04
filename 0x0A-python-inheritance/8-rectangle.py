#!/usr/bin/python3
"""base_geometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """ that raises an Exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates"""
        if not isinstance(name, str):
            return None
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """instantioation"""
        self.__width__ = width
        self.__height__ = height
        self.integer_validator("width", self.__width__)
        self.integer_validator("height", self.__height__)
