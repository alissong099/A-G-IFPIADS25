def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def obter_numero():
    try:
        num = int(input("Digite um número inteiro: "))
        return num
    except ValueError:
        print("Número inválido.")
        return obter_numero()

def main():
    num = obter_numero()
    if eh_primo(num):
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")

main()
