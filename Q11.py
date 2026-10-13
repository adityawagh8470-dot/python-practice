import pandas as pd

data = pd.Series([10,20,30,40,50,60,70,80,90,100]
)

print(data)
print(data[:4:])
print(data[2:7:])
print(data[-3::])
print(data[::-1])