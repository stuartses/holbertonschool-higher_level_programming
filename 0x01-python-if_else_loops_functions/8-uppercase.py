#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        asci = ord(str[i])
        chareq = str[i]
        if asci > 96 and asci < 123:
            chareq = chr(asci - 32)

        print("{}".format(chareq), end='')
    print()
