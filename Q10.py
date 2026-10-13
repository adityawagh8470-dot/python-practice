import pandas as pd
Employee_Salary = pd.Series([10000,20000,30000,40000,50000,60000],
    index = ["aditya", "varun", "vedant", "shantanu","prathamesh", "nayan"]
)

# df = pd.DataFrame(Employee_Salary)
# print(df)
# print("--------------------------------")
# print(df[df["salaries"]>40000])
# print("--------------------------------")
# print(df["salaries"].max())
# print("--------------------------------")
# print(df["salaries"].mean())
# print("--------------------------------")
# print(df["salaries"].add(2000))

print(Employee_Salary)
print("-----------------------")
print(Employee_Salary[Employee_Salary>40000])
print("-----------------------")
print(Employee_Salary.max())
print("-----------------------")
print(Employee_Salary.mean())
print("-----------------------")
print(Employee_Salary + 2000)





#
#
#
# employee_salary = pd.Series([],
#                             index = []
# )