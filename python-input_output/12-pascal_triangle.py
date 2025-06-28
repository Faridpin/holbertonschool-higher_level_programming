#!/usr/bin/python3
''' Pascal '''


def pascal_triangle(n):
    ''' function '''
    if n <= 0:
        return []
    pas = [[] for _ in range(n+1)]
    row2 = []
    for i in range(1, n+1):
        for j in range(i):
            if j == 0 or j == len(row2) :
                pas[i].append(1)
            else:
                pas[i].append(row2[j]+row2[j-1])
        row2 = pas[i]
    return pas
