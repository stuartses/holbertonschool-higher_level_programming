#!/bin/bash
# Get the Content Lenght of a http header
curl -s -I 0.0.0.0:5000 | grep "Content-Length" | awk -F ' ' '{print $2}'
