class O:

    @staticmethod
    def sum(a, b):
        return a + b

class MathOperations(O):

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

obj_ref = MathOperations()
output = obj_ref.div(10,5)
output2 = obj_ref.mul(10,5)
print(output)
print(output2)

print(MathOperations.sum(4,5))
print(MathOperations.sub(20,5))