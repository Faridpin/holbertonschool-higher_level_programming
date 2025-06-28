#!/usr/bin/python3
''' this file reads the file '''


def read_file(filename=""):
    ''' function '''
    with open(filename) as f:
        for line in f:
            print(line, end="")
