numbers = [12,18,25,31,42,50,63,70,85,90]
print(numbers[:4:])
print(numbers[2:8:])
print(numbers[-3::])
squares = [x**2 for x in numbers if x>40]
print(squares)
dict = {x: x**3 for x in numbers}
print(dict)
