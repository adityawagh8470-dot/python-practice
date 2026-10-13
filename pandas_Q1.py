import pandas as pd
data = {
    "name" : ["Rahul", "Pooja", "Amit", "Sneha", "Kiran"],
    "marks" : [72,88,65,94,58],
    "city" : ["Mumbai", "pune", "nashik", "mumbai", "pune"]
}

df = pd.DataFrame(data)
print(df)
print("----------------")
print(df[["name","city"]])
print("----------------")
print(df[df["marks"]>70])
print("--------------------")
print(df[df["marks"]==df["marks"].max()])
print(df["marks"].mean())

