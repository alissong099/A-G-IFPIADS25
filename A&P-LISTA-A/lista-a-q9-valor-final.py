# 09. Escreva um programa que aplique um desconto percentual sobre um preço inicial.

# entrada

preço1 = 100
preço2 = 200
preço3 = 500

# processamento

desconto1 = preço1 * 10 / 100
desconto2 = preço2 * 25 / 100
desconto3 = preço3 * 5 / 100

preço_final1 = preço1 - desconto1
preço_final2 = preço2 - desconto2
preço_final3 = preço3 - desconto3

# saída

print(f'O preço {preço1:.2f}R$ com desconto de 10% ficará por {preço_final1:.2f}R$')
print(f'O preço {preço2:.2f}R$ com desconto de 25% ficará por {preço_final2:.2f}R$')
print(f'O preço {preço3:.2f}R$ com desconto de 5% ficará por {preço_final3:.2f}R$')