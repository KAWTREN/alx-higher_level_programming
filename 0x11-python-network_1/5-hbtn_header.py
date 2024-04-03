#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""


if __name__ == '__main__':
    import sys
    import requests

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
