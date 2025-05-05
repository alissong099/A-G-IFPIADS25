def is_bissexto(ano):
    return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

def obter_ano():
    try:
        ano = int(input("Digite um ano: "))
        return ano
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return obter_ano()

def main():
    ano = obter_ano()
    if is_bissexto(ano):
        print(f"{ano} é bissexto.")
    else:
        print(f"{ano} não é bissexto.")

main()
