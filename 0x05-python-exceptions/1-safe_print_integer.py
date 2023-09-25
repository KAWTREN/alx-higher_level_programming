#!/usr/bin/python3
def safe_print_integer(value):
    try:
        format_value = "{:d}".format(int(value))
        print(format_value)
        return True
    except (ValueError, TypeError):
        return False
