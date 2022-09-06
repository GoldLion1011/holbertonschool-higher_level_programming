#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {
        'John': 12,
        'Alex': 8,
        'Bob': 14,
        'Mike': 14,
        'Molly': 16,
    }
    new_dict = 1
    for i in d:
        new_dict = new_dict * 2[i]
    return new_dict
