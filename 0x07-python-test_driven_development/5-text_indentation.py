#!/usr/bin/python3

"""4. Text indentation
This module prints a text with identation
Corresponds to Task 4.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

def text_indentation(text):
    """Function prints a text with 2 new lines after each of these characters:
       ., ? and :
    Args:
        text (str): Input string
    Returns:
        Prints String with indentation
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for x in range(len(text)):
        if text[x] == '.' or text[x] == '?' or text[x] == ':':
            print(text[x])
            print()
        else :
            if x > 0 and text[x] == ' ' and \
               (text[x - 1] == '.' or text[x - 1] == '?' or text[x - 1] == ':'):
                pass
            else:
                print(text[x], end='')
