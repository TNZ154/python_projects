"""
Write a program to create two classes Dog and Cat, with the same attributes -
 (name and age) and methods - (info and make_sound).
   Create different objects for each class and pass the parameters. 
   Showcase the concept of polymorphism in this program.

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print("Woof!")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print("Meow!")

a = Dog("Buddy", 3)
b = Cat("Whiskers", 2)

a.info()
a.make_sound()
b.info()
b.make_sound()