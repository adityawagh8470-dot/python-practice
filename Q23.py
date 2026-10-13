c=1
r=1
for i in range(15):
    print(2*c*r, end=" ")
    if c==r:
        print()
        r=r+1
        c=1
    else:
        c=c+1