def Casteo(List):
    Ar = []
    for x in List:
        Ar.append(int(x))
    return Ar

Array = input('3 Valores separados por comas ,: ')
Array = Casteo(Array.split(','))
Array.sort(reverse = True)
print(Array)