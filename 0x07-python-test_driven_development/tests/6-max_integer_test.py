#!/usr/bin/python3
"""unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test class for max_integer
    """

    def test_impty_list(self):
        """Test  that an empty list returns None"""
        self.assertIsNone(max_integer([]), "result should be none")
        
    def test_only_one_element_in_list(self):
        """Test only one element in list"""
        num = 2
        self.assertAlmostEqual(max_integer([num]), num,f"result should be {num}")
    def test_positives_list(self):
        """Test a positives list"""
        list_potives = [1, 3, 500, 7]
        self.assertAlmostEqual(max_integer([list_potives]), 500, "result should be 500")
    def test_nagatives_list(self):
        """Test a nagatives list"""
        lists_nagatives = [-1, -6, -700, -65]
        self.assertAlmostEqual(max_integer([lists_nagatives]), -1, "result should be -1")
        
    def test_nagatives_and_positives_list(self):
        """Test positive and nagative list"""
        lisst =[-2, 40, -59, 500]
        self.assertAlmostEqual(max_integer([lisst]), 500, "result should be 500")
        