#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_sorted = sorted(a_dictionary.keys())
    for i in a_sorted:
        print("{:s}: {}".format(i, a_dictionary[i]))
