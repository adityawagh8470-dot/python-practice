import pandas as pd
data ={
    "Name" : ["Arjun", "Meena", "Ravi", "Kavita", "Suresh", "Nisha"],
    "Maths": [78,92,65,85,58,88],
    "Python" : [82,89,72,91,64,95]
}

df = pd.DataFrame(data)
print(df)

print(df[df["Python"]>80][["Name","Python"]])
