#!/usr/bin/python3

"""
Fetch and url and get content
"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:")
print("\t- type: {}".format(type(html)))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(html.decode('utf-8')))
