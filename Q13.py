class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"name : {self.name}, salary : {self.salary}"

s1=Employee("aditya", 90000)
print(s1)
