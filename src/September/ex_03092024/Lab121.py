class Car:
    name = None
    make = None
    password = 123

    def __init__(self):
        self.password = "amith"

    def change_password(self):
        print(self.password)

obj_ref = Car()
print(obj_ref.password)
obj_ref.change_password()

# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.

class Car:
    model = None
    name = None
    password = 123

    def __init__(self):
        self.password = "pramod"

    def change_password(self):
        print(self.password)



object_ref = Car()
print(object_ref.password)
object_ref.change_password()