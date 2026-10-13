c=1
r=1
for i in range(21):
    print(c*r, end =" ")
    if c==r:
        print()
        r=r+1
        c=1
    else:
        c=c+1
