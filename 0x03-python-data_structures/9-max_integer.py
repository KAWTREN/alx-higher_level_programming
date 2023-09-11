#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    d = my_list[0]
    for i in my_list:
        if i > d:
            d = i
    return d
