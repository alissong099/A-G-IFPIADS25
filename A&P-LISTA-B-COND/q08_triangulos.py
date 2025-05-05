import math

def eh_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calcular_perimetro(a, b, c):
    return a + b + c

def calcular_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def classificar_lados(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    a, b, c = float(input("Lado A: ")), float(input("Lado B: ")), float(input("Lado C: "))
    if not eh_triangulo(a, b, c):
        print("Não é um triângulo válido.")
        return
    print(f"Perímetro: {calcular_perimetro(a, b, c)}")
    print(f"Área: {calcular_area(a, b, c):.2f}")
    print(f"Classificação: {classificar_lados(a, b, c)}")

main()
