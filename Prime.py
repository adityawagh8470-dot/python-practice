# mylist = [int(input("enter the number : ")) for i in range(1)]
# result = [x for x in mylist if x>1 and all(x%i!=0 for i in range(2,x))]
# if result:
#     print("prime")
# else:
#     print("not prime")
# #
# # result = [ x for x in range(10,101)
# #            if x>1 and all(x%i!=0 for i in range(2,x))]
# # if result:
# #     print("prime")
# #     print(result)
# # else:
# #     print("not prime")


# result= [x for x in range(10,101)
#          if x>1 and all(x%i!=0 for i in range(2,x))]
# print(result)

# num = int(input("enter the number : "))
# result = [ num for i in range(1) if num>1 and all(num%i!=0 for i in range(2,num))]
# if result:
#     print("prime")
# else:
#     print("not prime")

# mylist = [2,3,4,5,6,7,8,9,10]
# result = [x for x in mylist if x>1 and all(x%i!=0 for i in range(2,x))]
# print(result)
