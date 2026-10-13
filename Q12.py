import numpy as np
import pandas as pd
arr = np.array([10,20,30,40,50,60])
print(arr)
print(type(arr))
arr1 = pd.Series(arr)
print(arr1)
print(type(arr1))

print(arr1[arr1 > 40])

print(arr1.max())
print(arr1.mean())
