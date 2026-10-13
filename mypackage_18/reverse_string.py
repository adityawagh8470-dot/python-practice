# x = int(input("enter the number : "))
# # n = abs(x)
# # rev = 0
# # while n > 0:
# #     digit = n %10
# #     rev = rev*10 + digit
# #     n = n//10
# #
# # if x<0:
# #     rev = -rev
# #
# # if x< -2**31 or x> 2**31-1:
# #     print(0)
# # else:
# #     print(rev)


x = int(input("enter the number : "))
n = abs(x)
rev = 0
while n>0:
    digit = n % 10
    rev = rev*10+digit
    n = n//10

if x<0:
    rev = - rev

if x < -2**31 or x> 2**31-1:
    print(0)
else:
    print(rev)