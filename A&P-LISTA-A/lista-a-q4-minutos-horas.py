# 04. Escreva um programa que converta minutos para horas e minutos.

# entrada
minutos1 = 125
minutos2 = 90
minutos3 = 200
# processamento
horas1 = minutos1 // 60
horas2 = minutos2 // 60
horas3 = minutos3 // 60

minutos_rest1 = minutos1 % 60
minutos_rest2 = minutos2 % 60
minutos_rest3 = minutos3 % 60
# saída
print(f'{minutos1} minutos equivalem à {horas1} horas e {minutos_rest1} minutos')
print(f'{minutos2} minutos equivalem à {horas2} hora e {minutos_rest2} minutos')
print(f'{minutos3} minutos equivalem à {horas3} horas e {minutos_rest3} minutos')