#!/usr/bin/python3
"""base class modul"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """int
        args:
            id : int
        """
        if id is not None:
            self.id = id
        else:
            Bese.__nb_objects += 1
            self.id = Bese.__nb_objects
