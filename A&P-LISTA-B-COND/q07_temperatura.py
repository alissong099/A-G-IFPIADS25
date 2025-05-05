def validar_temperatura(valor, escala):
    if escala == "C":
        return valor >= -273.15
    elif escala == "K":
        return valor >= 0
    return True

def converter(temp, origem, destino):
    if origem == destino:
        return temp
    if origem == "C":
        if destino == "F":
            return temp * 9/5 + 32
        elif destino == "K":
            return temp + 273.15
    elif origem == "F":
        if destino == "C":
            return (temp - 32) * 5/9
        elif destino == "K":
            return (temp - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return temp - 273.15
        elif destino == "F":
            return (temp - 273.15) * 9/5 + 32

def main():
    orig = input("Origem (C/F/K): ").upper()
    dest = input("Destino (C/F/K): ").upper()
    temp = float(input(f"Temperatura em {orig}: "))
    if not validar_temperatura(temp, orig):
        print("Temperatura inválida!")
        return
    resultado = converter(temp, orig, dest)
    print(f"{temp:.2f}°{orig} = {resultado:.2f}°{dest}")

main()
