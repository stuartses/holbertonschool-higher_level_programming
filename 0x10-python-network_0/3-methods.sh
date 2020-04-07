#!/bin/bash
# get the allowed methods in header
curl -s -I "$1" | grep "Allow" | awk -F 'Allow: ' '{print $2}'
