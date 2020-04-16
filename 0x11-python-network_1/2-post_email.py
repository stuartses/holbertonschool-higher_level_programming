#!/usr/bin/python3

"""
Send a POST request
"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}

    # codification
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # request
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        content = response.read()

    print(content.decode('utf-8'))
