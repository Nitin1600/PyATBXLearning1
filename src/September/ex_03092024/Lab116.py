a = 10

class Person:
    b = 12
    c = 14

    def print_infor(self):
        global a
        a = "Hello"
        print(self.b)
        print(self.c)

obj_ref = Person()
obj_ref.print_infor()
print(a)
# print(c)

a = 10


class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class

    def print_infor(self):
        global a # Declare it as global
        a = "Hello"
        print(self.b)
        print(self.c)



object_Ref = Person()
object_Ref.print_infor()
print(a)
# print(b)