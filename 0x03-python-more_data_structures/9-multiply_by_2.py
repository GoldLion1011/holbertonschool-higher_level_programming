#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {
        'John': 12,
        'Alex': 8,
        'Bob': 14,
        'Mike': 14,
        'Molly': 16,
    }
    new_dict = []
    for k in a_dictionary:
        new_dict[k] = a_dictionary * 2[k]
    return new_dict
