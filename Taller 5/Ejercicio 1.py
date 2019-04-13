Archivo = open('Bytes.txt', 'w')
Archivo.write(input('Escribar cadena: \n'))
Archivo.close()
NumBytes = int(input('Bytes a leer: '))

#Lectura de bytes
Archivo = open('Bytes.txt', 'r')
linea = Archivo.read(NumBytes)
print(linea, "\n")
Archivo.close()