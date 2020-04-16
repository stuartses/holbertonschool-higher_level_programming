#!/usr/bin/python3

"""Print Error code using requests package"""

import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.ok:  # check if status is between 200 and 400
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
