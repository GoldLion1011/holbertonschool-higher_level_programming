#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nArgs = len(argv)
    if nArgs == 1:
        print("0 arguments.")
    elif nArgs == 2:
        print("1 argument.")
    else:
        print("{} arguments:".format(nArgs - 1))

    for i in range(1, nArgs):
        print("{}: {}".format(i, argv[i]))
