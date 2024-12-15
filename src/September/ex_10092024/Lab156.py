# class XYZ:
#     def f1(self):
#         try:
#             a = int(input("Enter a number: \n"))
#         except Exception as e:
#             print("Enter integers")
#         else:
#             print(a)
#         finally:
#             print("Finally: Anyhow i wil be printed")
#
# x = XYZ()
# x.f1()

class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number: \n"))
        except Exception as e:
            print("Enter integers")
        else:
            print(a)
        finally:
            print("Finally: Anyhow i wil be printed")

x = XYZ()
x.f1()