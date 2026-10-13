import pandas as pd
employee_salary= pd.Series ([20000,30000,40000,50000,60000,70000],
    index= ["aditya", "yash", "nayan", "shantanu", "shreekar", "pratham"]
)

print(employee_salary)
print("-----------")
print(employee_salary[employee_salary>40000])
print("---------")
print(employee_salary.max())
print("-----------")
print(employee_salary.mean())
print("---------------")
print(employee_salary+2000)



