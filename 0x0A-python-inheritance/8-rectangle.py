#!/usr/bin/python3
"""base_geometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    
    def __init__(self, width, height):
        """instantioation"""
        
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
