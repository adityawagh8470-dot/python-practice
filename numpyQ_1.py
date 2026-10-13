import numpy as np

marks = np.array([56,89,72,45,91,68,77])
print(marks)
print(marks[marks>70])
print("maximum marks : ", np.max(marks))
print("lowest marks : ", np.min(marks))
print(np.mean(marks))
print(marks + 5)