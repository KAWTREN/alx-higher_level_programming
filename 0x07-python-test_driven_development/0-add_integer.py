#!/usr/bin/python3
def add_integer(a, b=98):
    """
    adds two integers
    Args:
        a: first integers
        b: second integers
    Raise:
        TypeError: if a and b are not integers or float
    Return:
        sum: integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    A= int(a)
    B = int(b)
    sum = A + B
    return sum