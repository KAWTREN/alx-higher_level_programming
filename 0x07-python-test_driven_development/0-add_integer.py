#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add two integers.

    Args:
    a (int or float): The first integer or float.
    b (int or float, optional): The second integer or float. Defaults to 98.
    Return:
    int: The sum of a and b as integers.
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
