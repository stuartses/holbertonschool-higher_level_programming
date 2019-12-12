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

    print("{:d} {:s}".format(len_argv, str))

    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
