c=1
r=1
for i in range(1,22):
    if c%2==0:
        print(0, end=" ")
    else:
        print(1, end=" ")
    if c==r:
        print()
        r=r+1
        c=1
    else:
        c=c+1
