#!/usr/bin/python3

"""
Print the Error code
"""

from sys import argv
import urllib.request

try:
    with urllib.request.urlopen(argv[1]) as response:
        content = response.read()

    print(content.decode('utf-8'))

except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
