


class Person:

    def __init__(self):
        self.name = input("Enter the name:\n")
        self.age = input("Enter your age:\n")
        self.phone = input("Enter your phone number:\n")
        self.occupation = input("Enter your occupation\n")

    def enter_the_function_to_display(self):
        print(f"Name is {self.name}.", f"Age is {self.age}",
              f"Phone is {self.phone}", f"Occupation is {self.occupation}")

person1 = Person()

person1.enter_the_function_to_display()