import pandas as pd
data ={
    "Name" : ["Arjun", "Meena", "Ravi", "Kavita", "Suresh", "Nisha"],
    "Maths": [78,92,65,85,58,88],
    "Python" : [82,89,72,91,64,95]
}
df = pd.DataFrame(data)

print(df)
print("----------------------------------")
print(df[df["Python"]>80][["Name", "Python"]])
print("----------------------------------")
print(df[["Name","Maths"]])
print("----------------------------------")
print(df["Maths"].mean())
print("----------------------------------")
print("Heighest marks : " , df["Python"].max() , df["Maths"].max())
print("----------------------------------")
print(df[df["Python"]==df["Python"].max()][["Name", "Python"]])

