

class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1
        print("Hello")

    def sum(self):
        print("Sum wala Hello")
s1=Student()
s2=Student()
s3=Student()
s3.sum();
print("The number of students:",Student.count) 