#!/usr/bin/python3
"""square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """initialization method"""
        
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """__str"""
        
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"
    @property
    def size(self):
        """Getter size"""
        
        return self.height
    @size.setter
    def size(self, value):
        """Setter size"""
        
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        attr = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """returns dictionary """
        
        return  {'id': self.id,
                 'size': self.size, 
                 'x': self.x,
                 'y': self.y}