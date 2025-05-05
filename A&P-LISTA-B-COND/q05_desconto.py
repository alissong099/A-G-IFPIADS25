def desconto_base(valor):
    if valor > 500:
        return 0.15
    elif valor >= 200:
        return 0.10
    elif valor >= 100:
        return 0.05
    return 0.0

def desconto_adicional(vip, aniversario):
    desc = 0
    if vip:
        desc += 0.05
    if aniversario:
        desc += 0.03
    return desc

def preco_final(valor, vip, aniversario):
    total_desc = desconto_base(valor) + desconto_adicional(vip, aniversario)
    return valor * (1 - total_desc)

def main():
    valor = float(input("Valor da compra: R$ "))
    vip = input("Cliente VIP? (s/n): ").lower() == 's'
    aniversario = input("É aniversariante? (s/n): ").lower() == 's'
    final = preco_final(valor, vip, aniversario)
    print(f"Preço final: R$ {final:.2f}")

main()
