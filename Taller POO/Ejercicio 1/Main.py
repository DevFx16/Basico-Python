from Empleado import Empleado
import os

def Menu():
    return '''#############Menu#############
    1.Ver Atributos
    2.Setear Atributos
    3.Salir
    Seleccione un valor: '''
i = 0
emple = Empleado('Setea','Setea', 'Setea', 'Setea', 'Setea', 'Setea')
while i != 3:
    i = int(input(Menu()))
    if i == 1:       
        os.system('cls')
        print(f'Id: {emple.Id}')
        print(f'Nombre: {emple.Nombre}')
        print(f'Cargo: {emple.Cargo}')
        print(f'Salario: {emple.Salario}')
        print(f'Email: {emple.Email}')
        print(f'Telefono: {emple.Telefono}')
        input('Presione enter: ')
    elif i == 2:
        os.system('cls')
        emple.Id = input('Id: ')
        emple.Nombre = input('Nombre: ')
        emple.Cargo = input('Cargo: ')
        emple.Salario = input('Salario: ')
        emple.Email = input('Email: ')
        emple.Telefono = input('Telefono: ')
    elif i == 3:
        print('Bye Bye')