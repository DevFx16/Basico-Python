import os

loop = False
while loop == False:
    Texto = input('Texto: ')
    if(len(Texto) <= 0):
        os.system('cls')
        print('No debe ser valores nulos')
        loop = False
    else:
        os.system('cls')
        print(f'Primeros 2 {Texto[:2]}')
        print(f'Primeros 3 {Texto[:3]}')
        print(f'Invertir {Texto[::-1]}')
        loop = True
        pass
    pass