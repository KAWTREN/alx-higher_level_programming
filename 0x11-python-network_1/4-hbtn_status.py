#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status with package requests"""


if __name__ == '__main__':
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}\n\t- content: {response.text}")
