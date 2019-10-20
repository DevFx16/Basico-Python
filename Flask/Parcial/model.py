from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import relationship
from app import db


class Empleado(db.Model):
    """Empleados de la empresa"""
    __tablename__ = 'Empleado'

    Id = Column(String(20), primary_key=True)
    Tipo = Column(String(20), nullable=False)
    Nombres = Column(String(50), nullable=False)
    Apellidos = Column(String(50), nullable=False)
    Edad = Column(Integer, nullable=False)
    Email = Column(String(30), nullable=False)
    Profesion = Column(String(20), nullable=False)
    Telefono = Column(String(20), nullable=False)
    Cargo = Column(String(20), nullable=False)
    Salario = Column(Float, nullable=False)
    Image = Column(String(50), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
