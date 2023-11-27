#!/usr/bin/python3
"""1-Rectangle module"""


class Rectangle:
    """Rectangle class"""
    
    number_of_instances = 0
    print_symbol = "#"
   
    def __init__(self, width=0, height=0):
        self.width = width
        self.height= height
        Rectangle.number_of_instances += 1
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
    def area(self):
        """rectangle area"""
        return self.width * self.height
    def perimeter(self):
        """rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
    def __str__(self):
        """rectangle with charachter #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            s = ((self.width * f"{Rectangle.print_symbol}" + "\n") * self.height) .rstrip()
            return s
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)
    def __del__(self):
        """delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    