#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(j): None for j in 'cC'})
    return new_string
