class GrandParent:
    key_gold = "2Kg"
    def grand_parent(self):
        return "This grandpa's method"

class Parent(GrandParent):
    def parent(self):
        return "This is parent's method"

class Child(Parent):
    mac_m3_apple = "M3 MAX"
    def child(self):
        return "This is child's method"

child = Child()
print(child.grand_parent())