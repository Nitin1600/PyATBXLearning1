# class Dog:
#
#     def walk(self):
#         print("I am walking")
#
#     def bark(self):
#         print("bark")
#
#     def eat(self, food):
#         print("I am eating")
#
# dog1 = Dog()
# dog1.name = "Chow"
# print(dog1.name)
# dog1.walk()
# print(dog1.name)
#
# dog2 = Dog()
# dog2.name = "Mow"
# print(dog2.name)
# dog2.walk()
# print(dog2.name)

# dog3() == dog1()


class Dog: # class Name will always start from the Capital letter
    # A
    name = None
    breed = None
    color = None

    # B
    def sleep(self):
        print("Sleeping")

    def bark(self):
        print("bark")

    def eat(self,food):
        print(food)


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print(" ---- -----------------")


dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)

dog3 = dog1