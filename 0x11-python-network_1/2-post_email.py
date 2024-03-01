#!/usr/bin/python3
""" Python script that takes in a URL and an email address, sends a POST"""


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    data = {'email': sys.argv[2]}
    data = parse.urlencode(data).encode('utf-8')
    url = sys.argv[1]
    with request.urlopen(url, data=data) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
