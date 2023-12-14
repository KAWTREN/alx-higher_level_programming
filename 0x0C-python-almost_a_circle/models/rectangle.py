#!/usr/bin/python3
"""First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    
    
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """width getter"""
        
        return self.__width
    
    @width.setter
    def width(self, value):
        """width setter"""
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    @property
    def height(self):
        """height getter"""
        
        return self.__height
    @height.setter
    def height(self, value):
        """height setter"""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    @property
    def x(self):
        """x getter"""
        
        return self.__x
    @x.setter
    def x(self, value):
        """x setter"""
        
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    @property
    def y(self):
        """y getter"""
        
        return self.__y
    @y.setter
    def y(self, value):
        """y setter"""
        
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    def area(self):
        """rectangle area"""
        
        return self.__width * self.__height
    def display(self):
        """print in stdout the rectangle with the charachter #"""
        
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    def __str__(self):
        """__str__"""
        
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args, **kwargs):
        """update rectangle"""

        # change every attr to args value
        if args:
            # attr list
            attr_list = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not attribute in this class")
    def to_dictionary(self):
        """returns the dictionary representation"""
        
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}