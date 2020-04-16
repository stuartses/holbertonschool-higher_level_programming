#!/usr/bin/python3

"""Request in POST and get JSON"""

import requests
from sys import argv

if len(argv) == 1:
    q = ""
else:
    q = argv[1]

r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    r_json = r.json()
    if r_json == {}:
        print("No result")
    else:
        print("[{}] {}".format(r_json['id'], r_json['name']))

except ValueError:
    print("Not a valid JSON")
