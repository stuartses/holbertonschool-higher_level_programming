#!/usr/bin/python3

"""
Get X-Request-Id from Header in HTTP request
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        the_headers = response.info()

    print(the_headers.get('X-Request-Id'))
