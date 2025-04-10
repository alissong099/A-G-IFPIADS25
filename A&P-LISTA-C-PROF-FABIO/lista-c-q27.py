segundos = int(input("Digite os segundos: "))
horas = segundos // 3600
seg_rest = segundos % 3600
minutos = seg_rest // 60
seg_rest = seg_rest % 60
print(horas, "h", minutos, "min", seg_rest, "s")
