numero = int(input("Digite um número de 3 dígitos: "))
c = numero // 100
d = (numero % 100) // 10
u = numero % 10
inverso = u * 100 + d * 10 + c
print("Inverso:", inverso)
