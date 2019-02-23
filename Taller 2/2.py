def Triangular(Rango):
    Suma = 0
    for x in range(1, Rango + 1):
        Suma += x
    return Suma

Rango = int(input('Rango: '))
for x in range(1, Rango + 1):
    print(f'{x} ---> {Triangular(x)}')
    pass