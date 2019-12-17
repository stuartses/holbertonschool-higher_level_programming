#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_list = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    while (len(list_a) < 2):
        list_a.append(0)

    while len(list_b) < 2:
        list_b.append(0)

    add_list.append(list_a[0] + list_b[0])
    add_list.append(list_a[1] + list_b[1])

    add_tuple_res = tuple(add_list)
    return add_tuple_res
