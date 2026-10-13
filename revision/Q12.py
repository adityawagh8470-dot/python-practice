import numpy as np
import pandas as pd

arr = np.array([10,20,30,40,50,60])
marks = pd.Series(arr, index=["aditya", "rohan", "mohan", "rahul", "shubham","sejal"])
print(marks)
print("-------")
print(marks[marks>70])
print("-------")
print(marks.max())
print("-------")
print(marks.mean())
