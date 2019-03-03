import json

with open('./Data/Data.json', encoding='latin1') as fich:
    datos = json.load(fich)
    print(datos)