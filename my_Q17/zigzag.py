s = input("Enter string: ")
n = int(input("Enter rows: "))

if n == 1:
    print(s)
else:
    rows = [""] * n
    r = 0
    d = 1

    for ch in s:
        rows[r] += ch

        if r == 0:
            d = 1
        elif r == n - 1:
            d = -1

        r += d

    print("".join(rows))