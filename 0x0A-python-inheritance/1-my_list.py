#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """class MyList that inherites from list"""
    
    def __init__(self):
        super().__init__()
        
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))