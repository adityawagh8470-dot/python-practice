c=1
r=5
for i in range(1,16):
    print(" "*(5-r), end="")
    print("*", end=" ")
    if c==r:
        print()
        r=r-1
        c=1
    else:
        c=c+1