import sys
inp = int(sys.argv[1])
a = inp
while a>=1:
    if a == inp or a == 1:
        print("+",end="")
        i = inp
        while i > 1:
            print("--",end="")
            i-=1
        print("+")
        a-=1
    else:
        print("|",end="")
        i = inp
        while i > 1:
            print("  ",end="")
            i-=1
        print("|")
        a-=1
