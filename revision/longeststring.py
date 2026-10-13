s = input("Enter string: ")
sub = ""
m = 0

for ch in s:
    if ch in sub:
        sub = sub[sub.index(ch) + 1:]
    sub += ch
    m = max(m, len(sub))

print(m)