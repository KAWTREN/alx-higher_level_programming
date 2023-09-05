#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)%10
    if num < 0:
        num *= -1
    print(num, end= '')
    return num
