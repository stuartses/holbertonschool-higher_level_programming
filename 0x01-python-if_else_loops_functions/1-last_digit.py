#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = -number
else:
    new = number

last_digit = new % 10
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    str = 'and is greater than 5'
if last_digit == 0:
    str = 'and is 0'
if last_digit < 6 and last_digit != 0:
    str = 'and is less than 6 and not 0'
print('Last digit of {:d} is {:d} {}'.format(number, last_digit, str))
