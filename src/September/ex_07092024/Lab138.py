# class MathUtils:
#     # def add(self, a, b):
#     #     return  a + b
#     #
#     # def add(self, a, b, c):
#     #     return a + b + c
#
#     def add(self, a, b, c=4, d=2):
#         return a + b + c + d
#
# sum = MathUtils()
# op1 = sum.add(1,2)
# print(op1)

class MathUtils(object):  # is- A object - single inheritnace
    # Method - overloading - Not supported!
    # def add(self, a, b):
    #     return a + b
    #
    # def add(self, a, b, c):
    #     return a + b + c

    def add(self, a, b, c=10, d=1):
        return a + b + c + d


math = MathUtils()
op1 = math.add(1, 2)
print(op1)


