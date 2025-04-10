num = int(input("Digite um número de 4 dígitos: "))
milhar = num // 1000
centena = (num % 1000) // 100
dezena = (num % 100) // 10
unidade = num % 10
soma = milhar + centena + dezena + unidade
print("Soma dos dígitos:", soma)
