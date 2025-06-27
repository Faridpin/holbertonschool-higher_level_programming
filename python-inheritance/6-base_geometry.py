#!/usr/bin/python3
''' area method with exception '''


class BaseGeometry:
    ''' "BaseGeometry" class'''
    def area(self):
        raise Exception("area() is not implemented")
