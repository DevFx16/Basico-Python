repe = int(input('Numero de repeticiones: '))

nums = []
suma = 0
producto = 1

while repe > 0:
    nums.append(input('Numero: '))
    repe = repe - 1
    pass

for x in nums:
    suma = suma + float(x)
    producto = producto * float(x)
    pass

nums = sorted(nums)

print(f'Suma: {suma}\nProducto: {producto}\nMenor: {nums[0]}\nMayor: {nums[len(nums) - 1]}')