import csv

with open('./Data/Data.tsv', encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv, delimiter='\t')
    asociaciones = {}
    for linea in dict_lector:
        centro = linea['Asociacion']
        subvencion = float(linea['Importe'])
        if centro in asociaciones:
            asociaciones[centro] = asociaciones[centro] + subvencion
        else:
            asociaciones[centro] = subvencion
    print(asociaciones)