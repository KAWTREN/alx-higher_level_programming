#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """
        test Base class
    """

    def test_id_increasing(self):
        """
        test Base calss without arguments
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base(25)
        self.assertEqual(base2.id, 25)
        base3 = Base()
        self.assertEqual(base3.id, 2)

