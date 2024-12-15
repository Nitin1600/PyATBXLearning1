#Hierarchial Inheritance:

class Father:
    def BHK1(self):
        print("1BHK")

class Akash(Father):
    def BHK2(self):
        print("2BHK")

class Amith(Father):
    def BHK3(self):
        print("3BHK")

class Abhishek(Father):
    def no_house(self):
        print("no_house")

akash = Akash()
akash.BHK1()
akash.BHK2()

amith = Amith()
amith.BHK1()
amith.BHK3()
# amith.BHK2()