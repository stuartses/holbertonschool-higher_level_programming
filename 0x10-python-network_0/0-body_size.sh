#!/bin/bash
# Get the Content Lenght of a http header
curl -s -I "$1" | grep "Content-Length" | awk -F ' ' '{print $2}'
