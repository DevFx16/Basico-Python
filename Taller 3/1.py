import os

loop = False
while loop == False:
    Texto = input('Texto a encontrar: ')
    char = input('Caracter: ')
    if(len(Texto) <= 0 or len(char) <= 0):
        os.system('cls')
        print('No debe ser valores nulos')
        loop = False
    else:
        Texto = Texto.upper()
        char = char.upper()
        print(f'El numero de caracter {char} es: {Texto.count(char)}')
        loop = True
        pass
    pass
