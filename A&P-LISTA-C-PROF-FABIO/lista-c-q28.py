horas = int(input("Digite a quantidade de horas: "))
semanas = horas // (24 * 7)
dias = (horas % (24 * 7)) // 24
horas_rest = horas % 24
print(semanas, "semana(s),", dias, "dia(s),", horas_rest, "hora(s)")
