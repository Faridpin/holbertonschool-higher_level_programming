#!/usr/bin/python3
for i in range (0,98):
    print(f"{i} = 0x", end="")
    if i // 16 !=0:
        print(i//10, end="")
    if i%16<10:
        print(i%10)
    else:
        print(chr(i%10+97))
