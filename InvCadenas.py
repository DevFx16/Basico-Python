def InvertirOracion(Texto):
    Ar = Texto.split(' ')
    Inv = ''
    a = len(Ar) - 1
    while a >= 0:
        Inv += Ar[a] + ' '
        a = a - 1
        pass
    return Inv


def InvertirPalabras(Texto):
    Ar = Texto.split(' ')
    Inv = ''
    for item in Ar:
        P = ''
        a = len(item) - 1
        while a >= 0:
            P += item[a]
            a = a - 1
            pass
        Inv += P + ' '
        pass
    pass
    return Inv

Cadena = input('Texto: ')

print(InvertirOracion(Cadena))
print(InvertirPalabras(Cadena))
print(InvertirOracion(InvertirPalabras(Cadena)))
