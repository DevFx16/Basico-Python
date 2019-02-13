Var = 'Hola Mundo'

#Cambio de mayusculas y minisculas
print(Var.upper())
print(Var.lower())
print(Var.swapcase())
print(Var.capitalize())

#reemplazar
print(Var.replace('Hola', 'Texto Reemplazado'))

#Contar caracteres
print(Var.count('o'))

#Verificar estados
print(Var.startswith('Hola'))
print(Var.endswith('Mundo'))

#dividir string
print(Var.split())
print(Var.split('o'))

#buscar caractar index
print(Var.find('o'))

#Longitud
print(len(Var))

#verficar tipo
print(Var.isnumeric())
print(Var.isalpha())

#Los strings se puede tratar como listas

#Concatenaciones
print(f'Esto es un texto concatenado {Var}')
print('Texto {0}'.format(Var))