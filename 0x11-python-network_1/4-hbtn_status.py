#!/usr/bin/python3

"""
Fetch an url using Requests package
"""

import requests

r = requests.get('https://intranet.hbtn.io/status').text
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r))
