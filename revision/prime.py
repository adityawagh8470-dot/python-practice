# n = int(input("enter th enumber : "))
# result = [n for i in range(1) if n>1 and all(n%i!=0 for i in range(2,n))]
# if result:
#     print("Prime")
# else:
#     print("not prime")
#

result = [x for x in range(10,101) if x>1 and all(x%i!=0 for i in range(2,x))]
print(result)
