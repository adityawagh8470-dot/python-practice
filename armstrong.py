mylist = [int(input("enter the number : ")) for i in range(5)]
#
result = [x for x in mylist if x == sum(int(d)**3 for d in str(x))]
print(result)
# if result:
#     print("armstrong")
# else:
#     print("not armstrong")

# x = int(input("enter the number : "))
# result = [x for i in range(1) if x == sum(int(d)**3 for d in str(x))]
# if result:
#     print("armstrong")
# else:
#     print("not armstrong")
