#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


if __name__ == '__main__':
    import sys
    import requests

    data = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
