numero = int(input("Digite um número inteiro de 3 dígitos: "))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
soma = centena + dezena + unidade
print("Soma dos dígitos:", soma)
