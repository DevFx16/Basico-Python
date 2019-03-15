repe = int(input('Numero de repeticiones: '))

textos = []

while repe > 0:
    textos.append(input('Texto: '))
    repe = repe - 1
    pass

enc = input('Texto a encontrar: ')

print(f'Aparece en la lista {textos.count(enc)} veces')