class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"name : {self.name}, marks : {self.marks}"

    def result(self):
        if self.marks>=50:
            print("Pass")
        else:
            print("Fail")

s1= student("aditya", 50)
s2 = student("yash", 30)

print(s1)
s1.result()

print(s2)
s2.result()
