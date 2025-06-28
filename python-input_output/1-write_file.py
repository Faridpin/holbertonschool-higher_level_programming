#!/usr/bin/python3
''' this file writes to a file '''


def write_file(filename="", text=""):
    ''' function '''
    with open(filename, "w") as f:
        return f.write(text)
