#!/usr/bin/python3
print("{}".format('\n'.join(f"{i} = 0x{i:x}" for i in range(99))))

#for i in range (0,98):
#    print(i," = 0x", i//16 if i !=  0 else print(i), end="")
#    if i%16<10:
#        print(i%10)
#    else:
#        print(chr(i%10+97))
