# 10. Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.

# entrada

capital_inicial1 = 1000
capital_inicial2 = 500
capital_inicial3 = 2000

tempo1 = 6
tempo2 = 4
tempo3 = 12

# processamento

taxa_juros1 = 2 / 100
taxa_juros2 = 5 / 100
taxa_juros3 = 1 / 100

montante_final1 = capital_inicial1 + (capital_inicial1 * taxa_juros1 * tempo1)
montante_final2 = capital_inicial2 + (capital_inicial2 * taxa_juros2 * tempo2)
montante_final3 = capital_inicial3 + (capital_inicial3 * taxa_juros3 * tempo3)

# saída

print(f'O montante final será de R${montante_final1:.2f}')
print(f'O montante final será de R${montante_final2:.2f}')
print(f'O montante final será de R${montante_final3:.2f}')