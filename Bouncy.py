def Creciente(Num):
    r = False
    a = 0
    while r == False and a < len(Num) - 1:
        if int(Num[a]) <= int(Num[a + 1]):
            if a + 1 == len(Num) - 1 :
                r = True
        else:
            r = False
            break
        a = a + 1
    return r


def DeCreciente(Num):
    r = False
    a = 0
    while r == False and a < len(Num) - 1:
        if int(Num[a]) >= int(Num[a + 1]):
            if a + 1 == len(Num) - 1 :
                r = True
        else:
            r = False
            break
        a = a + 1
    return r


Num = input('Numero: ')
if Creciente(Num) == False and DeCreciente(Num) == False:
    print('Es Bouncy')
else:
    print('No Es Bouncy')
