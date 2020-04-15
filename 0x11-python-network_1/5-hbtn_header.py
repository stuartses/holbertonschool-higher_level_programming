#!/usr/bin/python3

"""
Get X-Request-Id using requets package
"""

from sys import argv
import requests

r = requests.get(argv[1])
print(r.headers['X-Request-Id'])
