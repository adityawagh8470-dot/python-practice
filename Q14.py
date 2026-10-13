class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age:{self.age}"

class student(Person):
    def __init__(self,name , age, course, marks):
        self.course = course
        self.marks = marks
        super().__init__(name, age)

    def __str__(self):
        return super().__str__() + f", course: {self.course}, marks : {self.marks}"

s1 = student("aditya", 22, "dbda", 90)
print(s1)