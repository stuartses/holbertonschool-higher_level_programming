#!/usr/bin/python
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{:d} {:s}".format(len(sys.argv) - 1, "arguments."))
    if len(sys.argv) == 2:
        print("{:d} {:s}".format(len(sys.argv) - 1, "argument:"))
    if len(sys.argv) > 2:
        print("{:d} {:s}".format(len(sys.argv) - 1, "arguments:"))

    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
