def validar_nota(nota):
    return 0 <= nota <= 10

def obter_nota(mensagem):
    try:
        nota = float(input(mensagem))
        if validar_nota(nota):
            return nota
        else:
            print("Nota fora do intervalo permitido.")
            return obter_nota(mensagem)
    except ValueError:
        print("Entrada inválida.")
        return obter_nota(mensagem)

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(notas):
    if 0 in notas:
        return "Reprovado (nota 0)"
    media = calcular_media(notas)
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    notas = [obter_nota(f"Digite a nota {i+1}: ") for i in range(3)]
    print(f"Média: {calcular_media(notas):.2f} - Situação: {verificar_situacao(notas)}")

main()
