#!/usr/bin/python3

"""
Access to GitHub Api using requests
Basic Authenication and personal access token
Is needed a token generated in github with read:user permission (only)
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    req = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(argv[1], argv[2]))

    print(req.json().get('id'))
