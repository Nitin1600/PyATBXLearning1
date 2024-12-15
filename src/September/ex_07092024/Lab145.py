class Excelreader():

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLDBConnection():

    @staticmethod
    def MySQLFile():
        print("Reading from MySQL")

class TC1():
    def runTC1(self):
        Excelreader().readExcelFile()
        MySQLDBConnection().MySQLFile()

tc1 = TC1()
tc1.runTC1()

class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:
    def runTC(self):
        ExcelReader().readExcelFile()
        MYSQLDBConnection.readMySQLFile()


tc1 = TC1()
tc1.runTC()