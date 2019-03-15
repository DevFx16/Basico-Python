lista = list(input('Ingrese la lista ejemplo 2,2,2 :  '))

repetido = []
unico = []
 
for x in lista:
    if x is not ',': 
        if lista.count(x) > 1:
            if x not in repetido:
                repetido.append(x)
        else:
            unico.append(x)   
 
print(f'Elementos unicos: {unico}')
print(f'Elementos repetidos: {repetido}')