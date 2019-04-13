from Person import Person

class Student(Person):

    def __init__(self, Program, Year, Fee, Name, Address):
        Person.__init__(self, Name, Address)
        self.Program = Program
        self.Year = Year
        self.Fee = Fee

    def getProgram(self):
        return self.Program
    
    def setProgram(self, Program):
        self.Program = Program

    def getYear(self):
        return self.Year
    
    def setYear(self, Year):
        self.Year = Year

    def getFee(self):
        return self.Fee

    def setFee(self, Fee):
        self.Fee = Fee

    def toString(self):
        return f'Student[Person[Name = {self.Name}, Address = {self.Address}, Program = {self.Program}, Year = {self.Year}, Fee = {self.Fee}]]'
    pass