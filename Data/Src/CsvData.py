import csv

with open('./Data/Data.csv', encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    next(lector, None)
    asociaciones = {}
    for linea in lector:
        centro = linea[0]
        subvencion = float(linea[2])
        if centro in asociaciones:
            asociaciones[centro] = asociaciones[centro] + subvencion
        else:
            asociaciones[centro] = subvencion
    print(asociaciones)