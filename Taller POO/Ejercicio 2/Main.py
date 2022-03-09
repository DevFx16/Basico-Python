from Estudiante import Estudiante
import os

def Menu():
    return '''#############Menu#############
    1.Ver Atributos
    2.Setear Atributos
    3.Salir
    Seleccione un valor: '''
i = 0
estudiante = Estudiante('Setea','Setea', 'Setea', 'Setea', 'Setea', 'Setea', 'Setea', 'Setea')
while i != 3:
    i = int(input(Menu()))
    if i == 1:       
        os.system('cls')
        print(f'Id: {estudiante.Id}')
        print(f'Tipo Identificacion: {estudiante.TipoIdentificacion}')
        print(f'Nombre: {estudiante.Nombre}')
        print(f'Programa: {estudiante.Programa}')
        print(f'Semestre: {estudiante.Semestre}')
        print(f'Email: {estudiante.Email}')
        print(f'Telefono: {estudiante.Telefono}')
        print(f'Institucion: {estudiante.Institucion}')
        input('Presione enter: ')
    elif i == 2:
        os.system('cls')
        estudiante.Id = input('Id: ')
        estudiante.TipoIdentificacion = input('Tipo Identificacion: ')
        estudiante.Nombre = input('Nombre: ')
        estudiante.Programa = input('Programa: ')
        estudiante.Semestre = input('Semestre: ')
        estudiante.Email = input('Email: ')
        estudiante.Telefono = input('Telefono: ')
        estudiante.Institucion = input('Institucion: ')
    elif i == 3:
        print('Bye Bye')