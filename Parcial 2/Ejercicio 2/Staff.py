from Person import Person


class Staff(Person):

    def __init__(self, School, Pay, Name, Address):
        Person.__init__(self, Name, Address)
        self.School = School
        self.Pay = Pay

    def getSchool(self):
        return self.School

    def setSchool(self, School):
        self.School = School

    def getPay(self):
        return self.Pay

    def setPay(self, Pay):
        self.Pay = Pay

    def toString(self):
        return f'Staff[Person[Name = {self.Name}, Address = {self.Address}, School = {self.School}, Pay = {self.Pay}]]'
    pass

    pass
