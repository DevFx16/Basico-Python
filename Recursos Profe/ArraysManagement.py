import os
def desplegarmenu():
	os.system('cls')
	print('		MENU')
	print('0. salir')
	print('1. Llenar nueva Lista(ingresar un dato al final)')
	print('2. Agregar dato en posicion')
	print('3. Borrar dato en posicion')
	print('4. Consultar posicion')
	print('5. Mostrar Lista actual')
	print('6. Invertir posicion')
	print('7. Ordenar posicion')
lista=[]
def llenar():
	lista.append(int(input('agregar un numero al final de la lista>>')))
def insertar():
	lista.insert((int(input('que numero de posicion quiere cambiar>>'))),(int(input('ingrese nuevo valor>>'))))
def borrar():
	lista.pop(int(input('que numero de posicion quiere Borrar>>')))
def inver():
	lista.reverse()
def orde():
	lista.sort()
while True:
	desplegarmenu()
	opc=input('insertar un numero')
	if opc=="1":
		llenar()
	elif opc=="2":
		insertar()
	elif opc=="3":
		borrar()
	elif opc=="4":
		print(lista[int(input('posicion que quiere ver(desde 0)>>'))])
		input('pulsa INTRO para continuar')
	elif opc=="5":
		print(lista)
		input('pulsa INTRO para continuar')
	elif opc=="6":
		inver()
	elif opc=="7":
		orde()
	elif opc=="0":
		input('FIN DEL PROGRAMA pulsa INTRO para continuar')
		break
	else:
		input('no has pulsado una opcion valida')
print('FIN')