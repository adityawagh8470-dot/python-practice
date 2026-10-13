class employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

    def __str__(self):
        return f"name:{self.name}, salary:{self.salary}"
e1= employee("aditya", 90000)
e2 = employee("rahul", 70000)

print(e1)
print(e2)

