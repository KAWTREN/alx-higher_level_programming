#!/usr/bin/python3
"""append_string"""
def append_write(filename="", text=""):
    """appends a string at the end of text file and returns the number of charachter"""
    with open(filename, 'a', encoding='utf-8') as file:
        return(file.write(text))