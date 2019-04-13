class Person:

    def __init__(self, Name, Address):
        self.Name = Name
        self.Address = Address

    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name
    
    def getAddress(self):
        return self.Address

    def setAddress(self, Address):
        self.Address = Address

    def toString(self):
        return f'Person[Name={self.Name}, Address={self.Address}]'
    
    pass
