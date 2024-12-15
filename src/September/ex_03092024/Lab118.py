class Person:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name

Amith = Person("Amith")
Akash = Person("Akash")
print(Amith.name)
print(Akash.name)
print("Who is walking with object Akash -> ", Akash.walk())

class Person:
    # Class Variables
    # Instance variables
    # name = "Amit" # hardcoded value
    def __init__(self, name):
        self.name = name

    def walk(self):
        return self.name


amit = Person("amit")
pramod = Person("pramod")
print(amit.name)
print(pramod.name)
print("Who is walking with the object pramod -> ", pramod.walk())