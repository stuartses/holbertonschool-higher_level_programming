#!/usr/bin/python
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv) - 1

    if len_argv == 0:
        str = "arguments."
    if len_argv == 1:
        str = "argument:"
    if len_argv > 1:
        str = "arguments:"

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
