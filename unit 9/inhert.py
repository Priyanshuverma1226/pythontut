


class alphabet:
    url="alphabet.com"
    def __init__(self):
        self.name="alphabet"


class Youtube(alphabet):
    url="youtube.com"
    def show(self):
        print(self.name)


class rank(Youtube):
    url="rank.youtube.com"

e1=rank()
e1.show()
print(e1.url)



# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# #child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d = Dog()
# d.bark()
# d.speak() 















