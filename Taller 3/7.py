repe = int(input('Numero de repeticiones: '))

nums = []
nums1 = []

while repe > 0:
    nums1.append(input('Caracter: '))
    nums.append(input('Cadena: '))
    repe = repe - 1
    pass

print(f'Lista 1: {nums}\nLista 2: {nums1}')