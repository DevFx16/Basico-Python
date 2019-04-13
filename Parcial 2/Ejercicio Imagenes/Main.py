Imagenes = open('listadoimagenes.txt', 'r')
a = 0
for linea in Imagenes.readlines():
    a = a + 1
    print(f'Imagen No. {a}: {linea}')

print(f'No. de Imagenes leidas: {a}')
