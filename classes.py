#Classes

from site import execusercustomize


class Point:        #In classes, first letter of each word in caps i.e. pascal naming convention
    def __init__(self,x,y): #constructor : init is used to initialise the object
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        # point1.x=11
        print("draw")


point1 = Point(10,20)

point1.draw()
print(point1.x)
#Constructor is a function that get called at the tim eof creating objects

# Exercise : Create class Person with name argument and talk() method

class Person:
    def __init__(self, name):  #name is the argument
        self.name = name
        # print("name")
    
    def talk(self): #talk is method
        print(f"hi, I am {self.name}")

person2 = Person("Ankana Saumya")
# person1.name()
# print(person2.name)
person2.talk()

person3 = Person("Anky") #Each object is different instance of Person class
person3.talk()
