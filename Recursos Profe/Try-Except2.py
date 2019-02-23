#Estructura try..except basica
try:
  print(x)
except:
  print("Una excepcion ha ocurrido")

#Definiendo un try...except para un error particular en python
try:
    print(x)
except NameError:
    print("Variable x no esta definida!!")    
except:
    print("Ha ocurrido un error imprevisto!!")

#Definiendo un bloque de codigo cuando no hay error
try:
  print("Hello")
except:
  print("Ha ocurrido un Error!!")
else:
  print("Ninguna Excepcion ha ocurrido")

#Uso de finallytry:
try:
  print(x)
except:
  print("Ha ocurrido una Excepcion!!")
finally:
  print("Ha finalizado el bloque try...except")
