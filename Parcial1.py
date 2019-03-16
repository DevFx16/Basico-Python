import os


def Listar():
    os.system('cls')
    for x in Elementos:
        print(x)
        pass


def Creación():
    os.system('cls')
    valor = ''
    while len(valor) <= 0:
        valor = input('Valor: ')
        if len(valor) <= 0:
            print('Valor no puede ser nulo')
        else:
            if valor in Elementos:
                print('Elemento duplicado')
            else:
                Elementos.add(valor)
                print('Creado')
        pass


def Editar():
    global Elementos
    os.system('cls')
    try:
        repe = int(input('Numeros de valor a mostrar: '))
        nums = []
        while repe > 0:
            nums.append(input('Valor: '))
            repe = repe - 1
        if '' in nums or None in nums:
            print('Nada de valores nulos')
            input('Presione Enter para continuar: ')
            Editar()
        else:
            Elementos = Elementos.update(set(nums))
            print('Editado')
    except:
        print('Solo numeros')
        input('Presione Enter para continuar: ')
        Editar()


def Borrar():
    valor = ''
    os.system('cls')
    while len(valor) <= 0:
        valor = input('Valor a borrar: ')
        if valor in Elementos:
            Elementos.remove(valor)
            print('Elemento borrado')
        else:
            print('Valor no encontrado')
            input('Presione Enter para continuar: ')
            Borrar()


def Union():
    os.system('cls')
    global Elementos
    try:
        repe = int(input('Numeros de valor a mostrar: '))
        nums = []
        while repe > 0:
            nums.append(input('Valor: '))
            repe = repe - 1
        if '' in nums or None in nums:
            print('Nada de valores nulos')
            input('Presione Enter para continuar: ')
            Union()
        else:
            Elementos = Elementos.union(set(nums))
            print('Unido')
    except:
        print('Solo numeros')
        input('Presione Enter para continuar: ')
        Union()


def Interseccion():
    os.system('cls')
    try:
        repe = int(input('Numeros de valor a mostrar: '))
        nums = []
        while repe > 0:
            nums.append(input('Valor: '))
            repe = repe - 1
        if '' in nums or None in nums:
            print('Nada de valores nulos')
            input('Presione Enter para continuar: ')
            Interseccion()
        else:
            print(f'Interseccion: {Elementos.intersection(set(nums))}')
    except:
        print('Solo numeros')
        input('Presione Enter para continuar: ')
        Interseccion()


def Diferencia():
    os.system('cls')
    try:
        repe = int(input('Numeros de valor a mostrar: '))
        nums = []
        while repe > 0:
            nums.append(input('Valor: '))
            repe = repe - 1
        if '' in nums or None in nums:
            print('Nada de valores nulos')
            input('Presione Enter para continuar: ')
            Diferencia()
        else:
            print(f'Diferencia: {Elementos.difference(set(nums))}')
    except:
        print('Solo numeros')
        input('Presione Enter para continuar: ')
        Diferencia()


def Ds():
    os.system('cls')
    try:
        repe = int(input('Numeros de valor a mostrar: '))
        nums = []
        while repe > 0:
            nums.append(input('Valor: '))
            repe = repe - 1
        if '' in nums or None in nums:
            print('Nada de valores nulos')
            input('Presione Enter para continuar: ')
            Ds()
        else:
            print(f'Diferencia simétrica: {Elementos.difference(set(nums))}')
    except:
        print('Solo numeros')
        input('Presione Enter para continuar: ')
        Ds()


def Menu():
    while True:
        os.system('cls')
        print('1: Ver Elementos\n2: Creación\n3: Editar\n4: Borrar\n5: Unión\n6: Intersección\n7: Diferencia\n8: Diferencia Simétrica\n9: Salir')
        opc = input('Elección: ')
        if opc is '1':
            Listar()
        elif opc is '2':
            Creación()
        elif opc is '3':
            Editar()
        elif opc is '4':
            Borrar()
        elif opc is '5':
            Union()
        elif opc is '6':
            Interseccion()
        elif opc is '7':
            Diferencia()
        elif opc is '8':
            Ds()
        elif opc is '9':
            print('BYE BYE')
            break
        else:
            print('Seleccione un valor correcto')
        input('Presione Enter para continuar: ')


Elementos = set([])
Menu()
