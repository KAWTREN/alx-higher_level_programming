#!/usr/bin/python3
"""1-Rectangle module"""


class Rectangle:
    """Rectangle class"""
   
    def __init__(self, width=0, height=0):
        self.width = width
        self.height= height
    @property
    def width(self):
        """width getter method"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """width setter methed"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """height getter"""
        return self.__height
    @height.setter
    def height(self, value):
        """height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value