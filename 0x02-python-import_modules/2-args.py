#!/usr/bin/python
import sys
len_argv = len(sys.argv) - 1

if len_argv == 0:
    str = "arguments."
if len_argv == 1:
    str = "argument:"
if len_argv > 1:
    str = "arguments:"

print("{} {}".format(len_argv, str))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
