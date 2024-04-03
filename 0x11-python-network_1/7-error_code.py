#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""


if __name__ == '__main__':
    import sys
    import requests

    response = requests.get(sys.argv[1])
    if (response.status_code < 400):
        print(response.text)
    else:
        print(f'Error code: {response.status_code}')
