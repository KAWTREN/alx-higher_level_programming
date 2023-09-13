#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tw = 0
    sc = 0
    for score, weight in my_list:
        tw += weight
        sc += score * weight
    return sc / tw
