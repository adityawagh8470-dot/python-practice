import numpy as np
expenses = np.array([12500, 9800, 14300, 11200, 15600, 10500])
print(expenses)
print(expenses[expenses > 11000])
print(np.sum(expenses))
print(np.mean(expenses))
print(np.max(expenses))
print( expenses + expenses*0.10)
print(expenses * 1.10)
