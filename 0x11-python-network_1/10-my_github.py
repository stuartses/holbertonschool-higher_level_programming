#!/usr/bin/python3

"""
Access to GitHub Api using requests
Basic Authenication and personal access token
Is needed a token generated in github with read:user permission (only)
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth

req = requests.get('https://api.github.com/users/stuartses',
                   auth=HTTPBasicAuth(argv[1], argv[2]))

req_dict = req.json()
print(req_dict['id'])
