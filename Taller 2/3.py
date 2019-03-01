def Costo(Tarifa, Num, Duracion):
    costo = 0
    for Llamada in Duracion:
        Segundos = Llamada.get('Hora') * 60 * 60 + Llamada.get('Minutos') * 60 + Llamada.get('Segundos')
        costo = Segundos * Tarifa
        pass
    return costo


Tarifa = float(input('Valor por segundo: '))
Num = int(input('Comunicaciones: '))
i = 0
Duracion = []
while i < Num:
    D = input('Hora:Minutos:Segundos : ')
    D = D.split(':')
    Duracion.append({
        'Hora': int(D[0]),
        'Minutos': int(D[1]),
        'Segundos': int(D[2])
    })
    i = i + 1
    pass
print(Costo(Tarifa, Num, Duracion))
