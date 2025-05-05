def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def obter_float(mensagem):
    try:
        return float(input(mensagem))
    except ValueError:
        print("Valor inválido.")
        return obter_float(mensagem)

def main():
    peso = obter_float("Digite seu peso (kg): ")
    altura = obter_float("Digite sua altura (m): ")
    imc = calcular_imc(peso, altura)
    print(f"IMC: {imc:.2f} - {classificar_imc(imc)}")

main()
