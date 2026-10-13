x = int(input("enter the number : "))
result = [x for i in range(1) if x == sum(int(d)**3 for d in str(x))]
if result:
    print("armstrong")
else:
    print("not armstrong")