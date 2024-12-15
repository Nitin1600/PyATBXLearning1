# class Dog:
#     name=None
#     age=None
#
#     def __init__(self,name,age):
#         print("Called,object is created")
#         self.name=name
#         self.age=age
#
#     def sleep(self):
#
#         print("Sleeping")
#         print("Who is sleeping -> ", self.name, self.age)
#         return None
#
# dog1 = Dog("Chow",10)
# print(dog1.name)
# dog1.sleep()
# #print(dog1.color)
# print(id(dog1))

# dog2 = Dog("Mow", 20)
# print(dog2.name)
# dog2.sleep()
# #print(dog2.color)
# print(id(dog2))

class Dog:
    name = None # Instance VARIABLE
    age = None
   # color = "Black" - Hardcoded - not generic to all - blueprint?

    def __init__(self, name, age):
        print("Called, Object is created")
        self.name = name
        self.age = age


    def sleep(self):
        local_variable = 10
        print("Sleeping")
        print("Who is sleeping -> ", self.name, self.age)
        return None


dog1 = Dog("chow", 10)
print(dog1.name)
dog1.sleep()
# print(dog1.color)
print(id(dog1))

dog2 = Dog("mow", 20)
print(dog2.name)
dog2.sleep()
# print(dog2.color)
print(id(dog2))