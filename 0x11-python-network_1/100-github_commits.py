#!/usr/bin/python3
"""takes your GitHub credentials uses the GitHub API to display your id"""


if __name__ == '__main__':
    import sys
    import requests
    import json

    response = requests.get(
        f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits')

    resp = response.json()
    for i in range(10):
        n = resp[i].get("commit").get("author").get("name")
        # response2 = requests.get(f'https://api.github.com/users/{n}')
        # resp2 = response2.json()
        print(f'{resp[i].get("sha")}: {n}')
