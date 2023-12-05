#!/usr/bin/python3
"""create object from a json file"""
import json
def load_from_json_file(filename):
    """creates an object from a json"""
    with open(filename, 'r', encoding= 'utf-8',) as file:
        return(json.load(file))