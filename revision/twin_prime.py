# for x in range(11,13):
#     a= x>1 and all(x%i!=0 for i in range(2,x))
#     b =(x+2) >1 and all((x+2)%i !=0 for i in range(2,x+2))
#
#
#     if a and b:
#         print(x, x+2)


# result = [ x for x in range(1,101) if x>1 and all(x%i!=0 for i in range(2,x))]
# print(result)
#
# x = int(input("enter the number : "))
# result = [x for i in range(1) if x>1 and all(x%i!=0 for i in range(2,x))]
# if result:
#     print("prime")
# else:
#     print("not prime")

# for x in range(11,13):
#     a = x>1 and all(x%i!=0 for i in range(2,x))
#     b = (x+2)>1 and all((x+2)%i!=0 for i in range(2,(x+2)))
#
#     if a and b:
#         print("twin prime", x, x+2)
#     else:
#         print("not twin prime")

# x= int(input("enter the number: "))
# y=int(input("enter the number: "))
#
# a= x>1 and all(x%i!=0 for i in range(2,x))
# b= y>1 and all(y%i!=0 for i in range(2,y))
#
# if a and b and abs( x-y )== 2:
#     print("twin prime")
# else:
#     print("not")
#
# x = int(input("enter the number : "))
# temp = x
# total = 0
# while x>0:
#     d = x%10
#     fact = 1
#     for i in range(1, d+1):
#         fact = fact * i
#     total = total+fact
#     x = x//10
# if total == temp:
#     print("special")
# else:
#     print("not")
