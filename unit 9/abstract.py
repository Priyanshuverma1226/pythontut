
class school:
    __count=0
    
    def __init__(sel,name):
        school.__name=name
        school.__count=school.__count+1
    def display(self):
        print("Student Name",school.__name)

s1=school("Tanish")
s2=school("Rohan")


# print(s2.__name)
s2.display()


