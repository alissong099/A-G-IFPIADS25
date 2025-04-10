num = int(input("Digite um número de 3 dígitos: "))
c = num // 100
d = (num % 100) // 10
u = num % 10
inverso = u * 100 + d * 10 + c
print("Diferença:", num - inverso)
