#Inheritance:

class Father:
    key = "2BHK"
    def Car(self):
        print("Father_Car", "Alto", self.key)

class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def Truck(self):
        print("Truck")

father_obj = Father()
father_obj.Car()
# print(father_obj.key2)
# father_obj.Truck()

son_obj = Son()
son_obj.Car()

# Inheritance

# class Father:
#     key = "2BHK"
#     def car(self):
#         print("Father Car!!", "ALTO",self.key)
#
#
# class Son(Father):
#     key2 = "3BHK"
#
#     def home(self):
#         print("3BHK")
#
#     def truck(self):
#         print("Truck")
#
#
# father_obj = Father()
# father_obj.car()
# # print(father_obj.key2)
# # father_obj.truck()
#
# son_obj = Son()
# son_obj.car()
