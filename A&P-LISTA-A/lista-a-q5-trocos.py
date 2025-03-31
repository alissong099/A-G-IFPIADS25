# 05. Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um
# determinado valor.

# entrada
valor1 = 130
valor2 = 70
valor3 = 90
# processamento

#Valor1

notas1_50 = valor1 // 50
resto1 = valor1 % 50
notas1_10 = resto1 // 10
resto1_10 = resto1 % 10

#Valor2

notas2_50 = valor2 // 50
resto2 = valor2 % 50
notas2_10 = resto2 // 10
resto2_10 = resto2 % 10

#Valor3

notas3_50 = valor3 // 50
resto3 = valor3 % 50
notas3_10 = resto3 // 10
resto3_10 = resto3 % 10

# saída 
print(f'Para o valor {valor1} são necessárias {notas1_50} notas de 50 e {notas1_10} notas de 10.')
print(f'Para o valor {valor2} são necessárias {notas2_50} nota de 50 e {notas2_10} notas de 10.')
print(f'Para o valor {valor3} são necessárias {notas3_50} nota de 50 e {notas3_10} notas de 10.')