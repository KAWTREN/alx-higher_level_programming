#!/usr/bin/python3
def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    Arsgs:
        obj: objet
    Return:
        list
    """
    return [atrb for atrb in dir(obj)]