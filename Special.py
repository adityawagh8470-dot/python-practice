# x = int(input("enter the number : "))
# temp = x
# total = 0
# while x>0:
#     d= x%10
#     fact = 1
#     for i in range(1, d+1):
#         fact = fact * i
#     total = total + fact
#     x=x//10
# if total == temp:
#     print("Special")
# else:
#     print("not special")
#
#
#
# x = int(input("enter the number : "))
# temp = x
# total = 0
# while x>0:
#   d= x%10
#   fact = 1
#   for i in range(1, d+1):
#           fact = fact * i
#   total = total + fact
#   x = x//10
# if total == temp:
#     print("Special")
# else:
#     print("Not special")
#
#     #145
#
# x = int(input("enter the number : "))
# temp = x
# total = 0
# while x>0:
#     d = x%10
#     fact = 1
#     for i in range(1, d+1):
#         fact = fact *i
#     total = total + fact
#     x=x//10
# if total == temp:
#     print("special")
# else:
#     print("not special")
#



x= int(input("enter the number: "))
temp = x
total =0
while x>0:
    d= x%10
    fact =1
    for i in range(1, d+1):
        fact = fact * i
    total = total + fact
    x= x//10
if total == temp:
    print("special number")
else:
    print("not special")