NumBouncy = 0
NoBouncy = 99
x = 99


def NumeroBouncy(num):
    CadNum = str(num)
    CadNumOrdenado = ''.join(sorted(list(CadNum)))
    return not(CadNum == CadNumOrdenado or CadNum == CadNumOrdenado[::-1])


while float(NumBouncy)/(NoBouncy + NumBouncy) < 0.99:
    x += 1
    if NumeroBouncy(x):
        NumBouncy += 1
    else:
        NoBouncy += 1
print(x)