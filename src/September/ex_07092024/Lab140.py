from abc import ABC, abstractmethod

class Father:
    def __init__(self, name):
        self.name = name

    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("Paid")

akash = Son("1L")
akash.loan()