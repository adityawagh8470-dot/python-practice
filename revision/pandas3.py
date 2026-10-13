import pandas as pd

data = {
    "Product": ["Pen", "Notebook", "Bag", "Bottle", "Calculator"],
    "Price": [20, 80, 750, 350, 600],
    "Quantity": [50, 30, 10, 25, 15]
}

df = pd.DataFrame(data)
print(df)

print(df[df["Price"]>300])
print(df[["Product", "Price"]])
print(df[df["Price"]==df["Price"].min()][["Product","Price"]])
print(df["Quantity"].sum())
