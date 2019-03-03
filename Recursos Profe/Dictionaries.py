#Un diccionario es una coleccion de datos no ordenada, indexada y que se puede modificar. 
# Los elementos se colocan como pares de claves y valores.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Creando un Diccionario vacio y posteriormente asignando sus elementos uno a uno
eng2sp = {}
print(type(eng2sp))
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

#Accediendo a los elementos de un diccionario
x = thisdict["model"]
y = thisdict.get("model")
print(x)
print(y)

#Modificar el valor especifico de un elemento del diccionario
thisdict["year"] = 2018
print(thisdict["year"])


#Iteracion en un Diccionario, para mostrar las claves del diccionario.
for x in thisdict:
  print(x)

#Imprimir todos los valores del Diccionario, uno por uno.
for x in thisdict:
  print(thisdict[x])

#Imprimir todos los valores del Diccionario, utilizando la funcion values()
for x in thisdict.values():
  print(x)

#Imprimir las claves y valores, utilizando la funcion items()
for x, y in thisdict.items():
  print(x, y)  

#Verificar si un elemento existe
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")  

#Longitud de un Diccionario
print(len(thisdict))

#Adicionar un elemento nuevo al Diccionario
thisdict["color"] = "red"
print(thisdict)


#Eliminar un determinado elemento del Diccionario
thisdict.pop("model")
print(thisdict)

#Eliminar el ultimo elemento insertado en el Diccionario
thisdict.popitem()
print(thisdict)


#Eliminar elementos con la funcion del()
del thisdict["year"]
print(thisdict)

#Vaciar el Diccionario
thisdict.clear()
print(thisdict)

#Eliminar el Diccionario Completamente
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

#Eliminar duplicados de una Lista en Python
mylist = ["a", "b", "a", "c", "c"] #Lista con elementos duplicados
mylist = list(dict.fromkeys(mylist)) #Se convierte primero a un Diccionario, y luego se reconvierte a una lista
print(mylist)