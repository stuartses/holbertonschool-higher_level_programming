#!/bin/bash
# send POST variables
curl "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
