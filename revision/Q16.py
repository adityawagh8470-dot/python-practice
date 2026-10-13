class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks= marks

    def __str__(self):
        return f"name :{self.name}, marks: {self.marks}"

    def result(self):
        if self.marks>=50:
            print("pass")
        else:
            print("fail")
s1 = student("aditya", 90)
s2 = student("shahu", 30)
s1.result()
s2.result()