#!/usr/bin/python3
''' this file writes to a file '''


def append_write(filename="", text=""):
    ''' function '''
    with open(filename, "a") as f:
        return f.write(text)
