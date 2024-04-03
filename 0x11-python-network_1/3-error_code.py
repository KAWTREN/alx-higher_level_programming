#!/usr/bin/python3
""" manage urllib.error.HTTPError"""


if __name__ == '__main__':
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
