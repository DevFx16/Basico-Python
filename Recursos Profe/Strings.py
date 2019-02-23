#Accesando cadenas de texto como lista de caracteres
var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#Actualizando una cadena de texto
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

#Cadena de Texto en varias lineas
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

#Funcion que retorna la primera letra de la cadena de texto en MAYUSCULAS
str = "this is string example....wow!!!"
print ("str.capitalize() : ", str.capitalize())

#Funcion que permite centrar una cadena de texto
str = "this is string example....wow!!!"
print ("str.center(40, 'a') : ", str.center(40, 'a'))

#Funcion que permite conocer la ocurrencia de una subcadena en otra cadena
str="this is string example....wow!!!"
sub='i'
print ("str.count('i') : ", str.count(sub))
sub='exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))

#Funcion que permite determinar si una cadena de texto termina en una subcadena indicada
Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))

#Funcion que permite determina si una cadena está presente en otra...devuelve el indice si es True. En caso contrario, -1
str1 = "this is string example....wow!!!"
str2 = "exam"
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))

#Funcion que permite determinar si una cadena tiene caracteres alfanumericos
str = "this2016" # No space in this string
print (str.isalnum())
str = "this is string example....wow!!!"
print (str.isalnum())

#Funcion que permite determinar si una cadena contiene unicamente caracteres alfabeticos.
str = "this"; # No space & digit in this string
print (str.isalpha())
str = "this is string example....wow!!!"
print (str.isalpha())

#Funcion que permite determinar si una cadena contiene unicamente digitos numericos.
str = "123456"; # Only digit in this string
print (str.isdigit())
str = "this is string example....wow!!!"
print (str.isdigit())

#Funcion que permite determinar si una cadena consiste unicamente de caracteres numericos
str = "this2016"
print (str.isnumeric())
str = "23443434"