#!/bin/bash
# send a header varaible
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
