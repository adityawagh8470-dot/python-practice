numbers = [12,18,25,31,42,50,63,70,85,90]

print(numbers[:4:])
print(numbers[2:8:])
print(numbers[-3::])

squares = [x**2 for x in numbers if x>40]
print(squares)

cube = {x: x**3 for x in numbers}
print(cube)
#
# [12, 18, 25, 31]
# [25, 31, 42, 50, 63, 70]
# [70, 85, 90]
# [1764, 2500, 3969, 4900, 7225, 8100]
# {12: 1728, 18: 5832, 25: 15625, 31: 29791, 42: 74088, 50: 125000, 63: 250047, 70: 343000, 85: 614125, 90: 729000}
#
# Process finished with exit code 0
