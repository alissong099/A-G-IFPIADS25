dias = int(input("Digite a idade em dias: "))
anos = dias // 365
dias_rest = dias % 365
meses = dias_rest // 30
dias_final = dias_rest % 30
print(anos, "ano(s),", meses, "mês(es),", dias_final, "dia(s)")
