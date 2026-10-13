import pandas as pd
numbers = pd.Series([10,20,30,40,50,60,70,80,90,100])

print(numbers)
print("----")
print(numbers [:4:])
print("----")
print(numbers[2:7:])
print("----")
print(numbers[-3::])
print("----")
print(numbers[::-1])
