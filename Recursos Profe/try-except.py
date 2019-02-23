dato=input('Ingrese un valor numerico: ')
try:
    numero=int(dato)
except:
    numero=-1
if numero>0 :
    print('El dato ingresado es numerico')
else:
    print('El dato ingresado no es numerico')