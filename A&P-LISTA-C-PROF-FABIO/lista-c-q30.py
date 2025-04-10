minutos = int(input("Digite o número de minutos: "))
dias = minutos // (24 * 60)
resto = minutos % (24 * 60)
horas = resto // 60
min_rest = resto % 60
print(dias, "dia(s),", horas, "hora(s),", min_rest, "minuto(s)")
