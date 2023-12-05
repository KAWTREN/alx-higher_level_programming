#!/usr/bin/python3
"""write_string"""

def write_file(filename="", text=""):
    """write a string and return the number of charachters written"""
    
    with open(filename, 'w', encoding= 'utf-8') as file:
        return(file.write(text))