#!/usr/bin/python3
"""rectangle class models"""

from models.Base import Base

class rectangle:
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init
        args:
        width: int
        height: int
        x: int
        y: int
        """
        super().__int__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """width getter"""
        return self.__width
    @width.setter
     def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """calcul rectangle area"""
        return self.width * self.height
    def display(self):
        """prints in stdout the Rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
    def __str__(self):
        """string"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args):
        """ssigns an argument to each attribute """
        if args:
            atrb_names = ["id", "width", "height", "x", "y"]
            for i, args in enumerate(atrb_names):
                setattr (self, atrb_names[i], args)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            else:
                raise ValueError(f"{key} is not attribute in this class")
        def to_dictionary(self):
            """dictionary representation of a Rectangle"""
            return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
