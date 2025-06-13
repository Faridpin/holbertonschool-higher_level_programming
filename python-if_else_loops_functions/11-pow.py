#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b>0:
        for i in range (0, b):
            c*=a
    else:
        for i in range (0, abs(b)):
            c /= a
    print(c)
pow(2, -2)
