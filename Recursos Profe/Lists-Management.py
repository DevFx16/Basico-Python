#Creacion de una Lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Acceso a los elementos
print(thislist[1])

#Cambiar el valor de un elemento
thislist[1] = "blackcurrant"
print(thislist)

#Iterar en una lista
for x in thislist:
  print(x)


#Verificar si un elemento de la lista existe
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Longitud de una Lista
print(len(thislist))

#Adicionar un elemento al final de la lista
thislist.append("orange")
print(thislist)

#Insertar un elemento en una posicion especifica de la lista
thislist.insert(1, "orange")
print(thislist)

#Eliminar un especificado elemento de la lista
thislist.remove("blackcurrant")
print(thislist)

#Elimina el indice especificado...si no se coloca , elimina el ultimo de la lista
thislist.pop()
print(thislist)

#Elimina el indice especificado
del thislist[0]
print(thislist)

#vaciar una lista
thislist.clear()
print(thislist)

#Eliminar la lista completamente
del thislist
#print(thislist)

#Copiar una lista
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print("Lista original:", fruits)
print("Copia de la Lista: ", x)

#Devolver el numero de elementos con un valor especificado en la lista
z = fruits.count("cherry")
print("cherry aparece ", z, " veces en la lista")

#Adicionar los elementos de una lista a otra lista
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print("Lista Extendida ", fruits)

#Reversa o inversa de una lista
print("Lista original ", fruits)
fruits.reverse()
print("Lista invertida ", fruits)

#Ordenar una lista
fruits.sort()
print("Lista ordenada ", fruits)