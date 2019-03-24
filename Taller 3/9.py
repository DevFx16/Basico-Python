N = int(input("Cuantos digitos quiere ingresar? "))
lista = []
lista2 = []
for i in range(N):
    lista.append(int(input("Digite un numero: ")))
    

print("Su lista es: ", lista)

for i in range(N):
    lista2.append(1*(lista[i]+1))

print("La segunda lista es: ", lista2)