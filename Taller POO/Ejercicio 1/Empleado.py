class Empleado:

    def __init__(self, Id, Nombre, Cargo, Salario, Email, Telefono, Empresa):
        self._Id = Id
        self._Nombre = Nombre
        self._Cargo = Cargo
        self._Salario = Salario
        self._Email = Email
        self._Telefono = Telefono
        self._Empresa = Empresa

    @property
    def Id(self):
        return self._Id

    @property
    def Nombre(self):
        return self._Nombre

    @property
    def Cargo(self):
        return self._Cargo
    
    @property
    def Salario(self):
        return self._Salario
    
    @property
    def Email(self):
        return self._Email

    @property
    def Telefono(self):
        return self._Telefono
    
    @property
    def Empresa(self):
        return self._Empresa

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    @Cargo.setter
    def Cargo(self, Cargo):
        self._Cargo = Cargo
    
    @Salario.setter
    def Salario(self, Salario):
        self._Salario = Salario
    
    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @Telefono.setter
    def Telefono(self, Telefono):
        self._Telefono = Telefono

    @Empresa.setter
    def Empresa(self, Empresa):
        self._Empresa = Empresa