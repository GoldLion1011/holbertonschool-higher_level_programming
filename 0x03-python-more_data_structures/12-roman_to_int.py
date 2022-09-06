#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        length = len(roman_string)
        romstr = roman_string
        num = 0
        nums = {
              "I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000
        }
        for i in range(length):
            if i + 1 < length nums[romstr[i]] < nums[romstr[i + 1]]:
                num -= nums[romstr[i]]
            else:
                num += nums[romstr[i]]
        return num
    return (0)
