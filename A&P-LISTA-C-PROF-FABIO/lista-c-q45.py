valor = int(input("Digite o valor do saque: "))
n50 = valor // 50
valor %= 50
n10 = valor // 10
valor %= 10
n5 = valor // 5
n1 = valor % 5
print("Notas de R$50:", n50)
print("Notas de R$10:", n10)
print("Notas de R$5:", n5)
print("Notas de R$1:", n1)
