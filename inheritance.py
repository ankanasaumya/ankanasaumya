class Mammal():
    def walk(self):     #common traits defined in this class which will be inherited 
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
# dog1.walk()
# print(dog1.bark())