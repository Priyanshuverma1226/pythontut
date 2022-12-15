class school:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Student Name",self.name)
    def show_age(self):
        print("Student Age",self.age)
s1=school("Tanish",15)
s2=school("Rohan",19)
s3=school("Manisha",20)
s4=school("jaspreet",12)
s3.show()
s3.show_age()
s2.show()
s5=school("Atish",20)
s5.show()
