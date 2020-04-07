#!/usr/bin/python3
""" Get the peak value in la list """


def find_peak(list_of_integers):
    """Return the peak integer in a unsorted list

    Argument:
        list_of_integers: input list
    Return:
        the peak integer
    """

    leng = len(list_of_integers)
    if leng == 0:
        return None

    # check the corners
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[leng - 1] > list_of_integers[leng - 2]:
        return list_of_integers[leng - 1]

    # trought list
    conts_peak = list_of_integers[0]
    for x in range(1, leng - 1):
        if list_of_integers[x] > list_of_integers[x - 1] and \
           list_of_integers[x] > list_of_integers[x + 1]:
            return list_of_integers[x]

        if list_of_integers[x] == list_of_integers[x - 1] and \
           list_of_integers[x] == list_of_integers[x + 1]:
            const_peak = list_of_integers[x]

    return const_peak
