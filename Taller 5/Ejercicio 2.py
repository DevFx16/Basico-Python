Archivo = open('texto2.txt', 'w')
num = int(input('Numero de cadenas a almacenar: '))
for i in range(num):
    Archivo.write(input() + '\n')
Archivo.close()