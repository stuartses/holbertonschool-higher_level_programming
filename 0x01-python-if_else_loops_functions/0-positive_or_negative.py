#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    str = 'is positive'
if number == 0:
    str = 'is zero'
if number < 0:
    str = 'is negative'
print('{} {}'.format(number, str))
