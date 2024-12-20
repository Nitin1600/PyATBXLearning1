from abc import ABC, abstractmethod

class Excelreader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(Excelreader):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Starting the browser")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("Excel is ready")

    def runTC1(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC1()

class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass


class TC1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


tc1 = TC1()
tc1.runTc()