from abc import ABC, abstractmethod

class Pycharm(ABC):

    @abstractmethod
    def payfees(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Subscriber(Pycharm):

    def payfees(self):
        print("Paid")

amith = Subscriber()
amith.payfees()