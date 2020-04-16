#!/usr/bin/python3

"""POST Request using request package"""

from sys import argv
import requests


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {'email': email}

    r = requests.post(url, data)
    print(r.text)
