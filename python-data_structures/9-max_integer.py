#!/usr/bin/python3
def max_integer(my_list=[]):
    a = min(my_list)
    for i in my_list:
        if a < i:
            a = i
    return a
