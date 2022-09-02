#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = ord(c)
        if upper >= 97 and upper <= 122:
            upper = upper - 32
        print("{}".format(upper), end="")
    print()
