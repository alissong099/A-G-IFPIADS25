# 06. Escreva um programa que receba um número de três dígitos e exiba ele invertido.

# entrada

número1 = 123
número2 = 450
número3 = 987

# processamento

# Número 1

centena1 = número1 // 100
dezena1 = (número1 % 100) // 10
unidade1 = (número1 % 100) % 10

inverso1 = (unidade1 * 100)+(dezena1 * 10)+centena1

# Número 2

centena2 = número2 // 100
dezena2 = (número2 % 100) // 10
unidade2 = (número2 % 100) % 10

inverso2 = (unidade2 * 100)+(dezena2 * 10)+centena2

# Número 3

centena3 = número3 // 100 
dezena3 = (número3 % 100) // 10
unidade3 = (número3 % 100) % 10

inverso3 = (unidade3 * 100)+(dezena3 * 10)+centena3

# saída
print(f'O inverso do número {número1} é: {inverso1}')
print(f'O inverso do número {número2} é: {inverso2}')
print(f'O inverso do número {número3} é: {inverso3}')