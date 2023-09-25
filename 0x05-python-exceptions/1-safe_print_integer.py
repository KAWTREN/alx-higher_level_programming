#!/usr/bin/python3
def safe_print_integer(value):
    try:
        fomat_value = "{:d}".format(int(value))
        print(format_value)
        return True
    except (valueError, typeError):
        return False
