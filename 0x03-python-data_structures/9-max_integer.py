#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0

    if my_list:
        for i in my_list:
            if i > a:
                a = i
        return a

    return None
