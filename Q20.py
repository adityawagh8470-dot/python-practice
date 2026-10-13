c=1
r=1
d=1
for i in range(25):
    print(c, end =" ")
    if c==r:
        print()
        if r==5:
            d= -1
        r=r+d
        c=1
    else:
        c=c+1
