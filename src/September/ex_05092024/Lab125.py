class Parent:
    gold = "2 Kg"

    def BHK2(self):
        print("2BHK")

class Son(Parent):
    diamond  = "Diamond"

    def BHK3(self):
        print("3BHK")

father_obj = Parent()
# print(father_obj.diamond)
# father_obj.BHK3()
print(father_obj.gold)
father_obj.BHK2()

son_obj = Son()
print(son_obj.diamond)
son_obj.BHK3()
print(son_obj.gold)
son_obj.BHK2()