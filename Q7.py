import numpy as np

arr = np.array([15,25,35,45,55,65,75,85])

print(arr[:5:])
print(arr[-3::])
print( arr[arr>40])
print( np.sum(arr), np.mean(arr))
square = arr**2
print(square)

