num = int(input("Digite el limite de numero de la susecion: "))

def fib(n):
    a, b = 0,1
    for i in range(n):
        print(a)
        a, b = b, a + b
def Prim(n):
    print("\nNumeros primos")
    for i in range(n):
        if i % 2 == 0:
            print(i)
fib(num)
Prim(num)