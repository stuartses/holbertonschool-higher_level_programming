#!/usr/bin/python3

"""
Get X-Request-Id from Header in HTTP request
"""

import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    the_headers = dict(response.headers._headers)

# Check if the header X-Request-Id exists
try:
    print(the_headers['X-Request-Id'])
except:
    pass
