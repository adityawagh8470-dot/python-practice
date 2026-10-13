marks = {
    'java':78, 'python':85, 'sql':65, 'linux':72, 'cloud':55
}

for key, value in marks.items():
    print(key, ":", value)

subjects = {subject : mark for subject, mark in marks.items() if mark> 70}
print(subjects)

subject = [x for x in marks.keys()]
print(subject)

heighest = max(marks.values())
print(heighest)

