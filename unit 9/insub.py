

class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2(Calculation1):
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
c1=Calculation1()
print(d.Summation(5,6))
print(d.Multiplication(5,4))
print(d.Divide(5,5))
print(issubclass(Derived,Calculation2))
print(issubclass(Derived,Calculation1))
print(issubclass(Calculation1,Calculation2))
print(isinstance(d,Derived))
print(isinstance(c1,Calculation1))