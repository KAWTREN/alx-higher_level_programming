#!/usr/bin/python3
class MyList(list):
    def __init__(self):
        super().__init__()
        
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))