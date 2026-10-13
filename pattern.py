# c=1
# r=5
# for i in range(15):
#     print(c, end=" ")
#     if c==r:
#         print()
#         r=r-1
#         c=1
#     else:
#         c=c+1

# c = 1
# r = 1
#
# for i in range(15):
#     print(" " * (5 - r), c, end=" ")
#
#     if c == r:
#         print()
#         r = r + 1
#         c = 1
#     else:
#         c = c + 1


# c=1
# r=1
# for i in range(25):
#     print(chr(96+r), end=" ")
#     if c==r:
#         print()
#         r=r+1
#         c=1
#     else:
#         c=c+1



# c=1
# r=1
# for i in range(1,16):
#     print(r, end=" ")
#     if c==r:
#         print()
#         r=r+1
#         c=1
#     else:
#         c=c+1


x = int(input("Enter the number: "))
temp = x
total = 0
while x>0:
    d=x%10
    fact = 1
    for i in range(1, d+1):
        fact = fact * i
    total = total + fact
    x = x//10
if total == temp:
    print("special")
else:
    print("not special")