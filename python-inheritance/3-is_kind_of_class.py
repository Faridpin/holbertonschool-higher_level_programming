#!/usr/bin/python3
''' This file checks if the object is the instance of class or subclass'''


def is_kind_of_class(obj, a_class):
    ''' method '''
    if isinstance(obj, a_class):
        return True
    return False
