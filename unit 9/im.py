class school:
    '''
    This class to add students
    '''
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
print(getattr(s1,'name'),':',getattr(s1,'age'))
setattr(s1,'age',21)
print(getattr(s1,'name'),':',getattr(s1,'age'))
print(hasattr(s1,'dob'))
print(s1.__dict__)

print(s1.__doc__)
print(s1.__module__)