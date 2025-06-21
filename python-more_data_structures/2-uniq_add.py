#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique_elements = []
    for i in my_list:
        if i in unique_elements:
            continue
        else:
            unique_elements.append(i)
            result += i
    return result
