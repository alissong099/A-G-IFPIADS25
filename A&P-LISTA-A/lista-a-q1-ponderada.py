# 01. Escreva um programa que calcule a média ponderada de três notas, considerando seus respectivos 
# pesos.

# entrada
#Aluno 1
nota1_1 = 8
nota2_1 = 7
nota3_1 = 6

peso1_1 = 2
peso2_1 = 3
peso3_1 = 5

#Aluno 2
nota1_2 = 10
nota2_2 = 5
nota3_2 = 8

peso1_2 = 4
peso2_2 = 2
peso3_2 = 4

#Aluno 3
nota1_3 = 3
nota2_3 = 7
nota3_3 = 10

peso1_3 = 1
peso2_3 = 1
peso3_3 = 2

# processamento
média_ponderada_aluno1 = ((nota1_1 * peso1_1) + (nota2_1 * peso2_1) + (nota3_1 * peso3_1)) / (peso1_1 + peso2_1 + peso3_1)
média_ponderada_aluno2 = ((nota1_2 * peso1_2) + (nota2_2 * peso2_2) + (nota3_2 * peso3_2)) / (peso1_2 + peso2_2 + peso3_2)
média_ponderada_aluno3 = ((nota1_3 * peso1_3) + (nota2_3 * peso2_3) + (nota3_3 * peso3_3)) / (peso1_3 + peso2_3 + peso3_3)
#saída
print(f'Aluno 1: Média ponderada = {média_ponderada_aluno1:.1f}')
print(f'Aluno 2: Média ponderada = {média_ponderada_aluno2:.1f}')
print(f'Aluno 3: Média ponderada = {média_ponderada_aluno3:.1f}')