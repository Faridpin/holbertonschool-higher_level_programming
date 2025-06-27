#!/usr/bin/python3
''' print the sorted list '''



class MyList(list):
    ''' MyList class '''
    def print_sorted(self):
        print(sorted(self))
