#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    count = 0
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for arg in (args):
        count+=1
        print(f"{count}: {arg}")
