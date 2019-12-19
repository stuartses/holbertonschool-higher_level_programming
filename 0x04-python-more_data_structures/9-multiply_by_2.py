#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new = {x: a_dictionary[x] * 2 for x in a_dictionary}
    return (a_new)
