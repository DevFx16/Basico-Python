def Conversor(Valor, Pesos):
    return Valor * Pesos

Pesos = float(input('Valor: '))
print(f'Dolares: {Conversor(0.00032, Pesos)}')
print(f'Euros: {Conversor(0.00028, Pesos)}')
print(f'Bitcoin: {Conversor(0.00000008, Pesos)}')