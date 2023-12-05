#!/usr/bin/python3
"""from json string to object"""
import json
def from_json_string(my_str):
    """returns an object represented bby json string"""
    return (json.loads(my_str))