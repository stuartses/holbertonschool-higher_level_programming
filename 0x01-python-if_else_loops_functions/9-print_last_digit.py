#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new = -number
    else:
        new = number
    last_digit = new % 10
    print("{}".format(last_digit), end='')

    return last_digit
