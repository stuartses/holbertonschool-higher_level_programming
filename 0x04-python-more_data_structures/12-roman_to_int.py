#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_res = 0

    for i in range(len(roman_string)):
        roman_value = romans[roman_string[i]]

        if i < len(roman_string) - 1:
            roman_value_next = romans[roman_string[i + 1]]
        else:
            roman_value_next = 0

        if roman_value_next > roman_value:
            int_res += -roman_value
        else:
            int_res += roman_value

    return int_res
