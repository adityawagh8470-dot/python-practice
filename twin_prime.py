# for x in range(10, 100):
#     a = all(x % i != 0 for i in range(2, x))
#     b = all((x + 2) % i != 0 for i in range(2, x + 2))
#
#     if a and b:
#         print(x, x + 2)


for x in range(10,101):
    a = x>1 and all(x%i!=0 for i in range(2,x))
    b = x>1 and all((x+2)%i!=0 for i in range(2,x+2) )

    if a and b:
        print(x, x+2)

