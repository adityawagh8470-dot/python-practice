import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
print(arr[arr>75])
print(arr[arr<40])
print(np.max(arr), np.min(arr))

print(np.mean(arr))
new = arr + 5
print(new)
