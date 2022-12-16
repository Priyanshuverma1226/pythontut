# class  animal:
#     def speak(self):
#         print("speaking")

# class dog:
#     def speak(self):
#         print("Branking")

# d=dog()
# a=animal()
# a.speak()
# d.speak()


class bank:
    def rate(self):
        return 10
class hdfc(bank):
    def rate(self):
        return 8
class punjab(bank):
    def rate(self):
        return 5

c=bank()
a=hdfc()
b=punjab()
print(a.rate())
print(b.rate())
print(c.rate())