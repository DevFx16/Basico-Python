#Los conjuntos son una coleccion de datos desorganizados y no indexados
#creacion de un conjunto
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Acceder a los elementos del conjunto
for x in thisset:
  print(x)

#Verificar si un elemento esta presente en el conjunto
print("banana" in thisset)

#Insertar(al final) un elemento en un conjunto
thisset.add("orange")
print(thisset)

#Adicionar varios elementos a un conjunto
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#Determinar la longitud de un conjunto
print(len(thisset))

#Eliminacion de un elemento de un conjunto con remove(). Si el elemento no existe, genera una excepcion.
thisset.remove("banana")
print(thisset)

#Eliminacion de un elemento de un conjunto con discard(). Si el elemento no existe, no genera excepcion.
thisset.remove("mango")
print(thisset)

'''Eliminacion de un elemento de un conjunto con pop(). Este siempre elimina el ultimo elemento, 
teniendo en cuenta que los conjuntos son estructuras no ordenadas, no es posible saber cual es. '''
x = thisset.pop()
print(x)
print(thisset)

#Vaciar un conjunto
thisset.clear()
print(thisset)

#Borrar un conjunto definitivamente
del thisset
print(thisset)
