#!/usr/bin/python3
def  print_square(size):
    """
    print a square with the caracter #
    Args:
        size: integer
    Raise:
        TypeError: if size is not integer
        ValueError: if size is  less than 0
        TypeError: if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <0:
        raise ValueError("size must be >= 0")
    """if size in (float, size < 0):
        raise TypeError("size must be an integer")"""
    for i in range(size):
        print("#" * size)