import re

def tamanho_minimo(senha):
    return len(senha) >= 8

def tem_maiuscula(senha):
    return any(c.isupper() for c in senha)

def tem_minuscula(senha):
    return any(c.islower() for c in senha)

def tem_numero(senha):
    return any(c.isdigit() for c in senha)

def tem_especial(senha):
    return any(c in "!@#$%&*" for c in senha)

def senha_valida(senha):
    return (tamanho_minimo(senha) and tem_maiuscula(senha) and 
            tem_minuscula(senha) and tem_numero(senha) and tem_especial(senha))

def obter_senha():
    senha = input("Digite a senha: ")
    if senha_valida(senha):
        print("Senha válida!")
    else:
        print("Senha inválida. Tente novamente.")
        obter_senha()

obter_senha()
