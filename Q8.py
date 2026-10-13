import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
print("> 75 : ", arr[arr>75])
print("<40 : ", arr[arr<40])
print("heighest : ", np.max(arr))
print("lowest : ", np.min(arr))
print("average : ", np.mean(arr))
new_arr = arr + 5
print("grace 5 : ",new_arr )