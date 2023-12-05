#!/usr/bin/python3
"""save object to file"""
import json
def load_from_json_file(filename):
    """writes an object to a text file using a json"""
    with open(filename, 'r', encoding= 'utf-8',) as file:
        return(json.load(file))