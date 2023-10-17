#!/usr/bin/python3
"""unitest for rectangle class"""

import unittest

from models.rectangle import Rectangle
from models.base import Base
import json

class TestRectangle(unittest.TestCase):
    """check if Rectangle inherited from Base class"""
    def test_inherit(self):
        """check if Rectangle inherited from Base class"""
        r = Rectangle(10,20)
        self.assertEqual(isinstance(r, Base), True)
    
