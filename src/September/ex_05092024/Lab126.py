#Multi-level Inheritance:

class GrandFather:
    gold = "2Kg"

    def BHK1(self):
        print("1BHK")

class Father(GrandFather):
    diamond = "22karat"

    def BHK2(self):
        print("2BHK")

class Son(Father):
    btc = "1BTC"

    def BHK3(self):
        print("3BHK")

s= Son()
f = Father()
gf = GrandFather()