def square(x):
    return x**2

def calculate(func, num):
    return func(num)

result = calculate(square, 5)
print(result)