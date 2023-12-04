#!/usr/bin/python3
"""base_geometry"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """init"""
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__(self, self.__size, self.__size)    
    def area (self):
        """calculates area"""
        return (self.__size) ** 2
    def __str__(self):
        """square string"""
        return f"[Square] {self.__size}/{self.__size}"
