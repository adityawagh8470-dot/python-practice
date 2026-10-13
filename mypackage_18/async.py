
x = int(input("Enter a number: "))
n = abs(x)
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if x < 0:
    rev = -rev

if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)
