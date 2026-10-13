import pandas as pd
data= {
    "Name": ["Rohan","Neha", "Vijay","Priya","Akash"],
    "Department" : ["It","HR","Finance", "IT","HR"],
    "Salary" : [48000, 42000, 55000, 62000, 39000]
}

df = pd.DataFrame(data)
print(df)

print(df[["Name","Department"]])

print(df[df["Salary"]>45000])

print(df[df["Salary"]==df["Salary"].min()])

print(df["Salary"].mean())