#!/usr/bin/python3
''' Checks if the object is the instance of subclasses '''


def inherits_from(obj, a_class):
    ''' mehtod '''
    if not type(obj) is a_class and isinstance(obj, a_class):
        return True
    return False
