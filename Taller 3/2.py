import os

loop = False
Vocales = ['A', 'E', 'I', 'O', 'U']
while loop == False:
    Texto = input('Texto a encontrar: ')
    if(len(Texto) <= 0):
        os.system('cls')
        print('No debe ser valores nulos')
        loop = False
    else:
        os.system('cls')
        Texto = Texto.upper()
        for Vocal in Vocales:
            print(f'El numero de caracter {Vocal} es: {Texto.count(Vocal)}')
            pass
        loop = True
        pass
    pass