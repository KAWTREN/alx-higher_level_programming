#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable"""


if __name__ == '__main__':
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
