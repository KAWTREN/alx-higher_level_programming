#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    say my name
    Args:
        first_name: string
        last_name: string
    Raise:
        TypeError: if first name or last name is not a sring
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    my_name = "My name is {} {}".format(first_name, last_name)if last_name else "My name is {}".format(first_name)
    print(my_name)