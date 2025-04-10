def calcular_saldo_atrasado(saldo_devedor, meses_atraso, juros_rotativo=0.12, juros_mora=0.01, multa=0.02):
    """Calcula o saldo atualizado após os meses de atraso com juros compostos"""
    
    saldo_inicial = saldo_devedor * (1 + multa)  # Aplica a multa de 2%
    saldo_final = saldo_inicial * ((1 + juros_rotativo + juros_mora) ** meses_atraso)  # Aplica juros compostos
    
    return saldo_final

def calcular_percentual_crescimento(valor_inicial, valor_final):
    """Calcula o percentual de crescimento da dívida, evitando divisão por zero"""
    if valor_inicial == 0:
        return 0  # Se não há saldo devedor, a dívida não cresceu
    return ((valor_final - valor_inicial) / valor_inicial) * 100

def coletar_dados():
    """Solicita e retorna os dados do usuário"""
    print("\n" + "="*40)
    print("💳 SIMULADOR DE FATURA DO CARTÃO 💳")
    print("="*40 + "\n")

    fatura = float(input("🔹 Digite o valor total da fatura (R$): "))

    # Coletando valores de pagamento e meses sem pagar
    p1 = float(input("\n💰 Opção 1: Quanto você pode pagar agora? R$ "))
    meses_p1 = int(input("📅 Quantos meses sem pagar após a opção 1? "))

    p2 = float(input("\n💰 Opção 2: Outra simulação de pagamento (R$): "))
    meses_p2 = int(input("📅 Quantos meses sem pagar após a opção 2? "))

    return fatura, p1, meses_p1, p2, meses_p2

# 🎉 Coletando os dados do usuário
fatura, p1, meses_p1, p2, meses_p2 = coletar_dados()

# 📌 Cálculo dos saldos devedores
saldo_p1 = calcular_saldo_atrasado(fatura - p1, meses_p1) if p1 < fatura else 0
saldo_p2 = calcular_saldo_atrasado(fatura - p2, meses_p2) if p2 < fatura else 0

# 📌 Cálculo dos percentuais de crescimento da dívida
percentual_p1 = calcular_percentual_crescimento(fatura - p1, saldo_p1)
percentual_p2 = calcular_percentual_crescimento(fatura - p2, saldo_p2)

# 📌 Exibição dos resultados
print("\n" + "="*40)
print("📊 RESULTADO DA SIMULAÇÃO 📊")
print("="*40 + "\n")

print(f"💰 Opção 1: Você pagou **R$ {p1:.2f}**")
if saldo_p1 == 0:
    print("   ✅ Você pagou tudo! Sem juros acumulados.")
else:
    print(f"   📆 Após **{meses_p1} meses**, sua dívida será de **R$ {saldo_p1:.2f}**")
    print(f"   🚀 A dívida cresceu **{percentual_p1:.2f}%**\n")

print(f"💰 Opção 2: Você pagou **R$ {p2:.2f}**")
if saldo_p2 == 0:
    print("   ✅ Você pagou tudo! Sem juros acumulados.")
else:
    print(f"   📆 Após **{meses_p2} meses**, sua dívida será de **R$ {saldo_p2:.2f}**")
    print(f"   🚀 A dívida cresceu **{percentual_p2:.2f}%**\n")

print("="*40)
print("⚠️ Lembre-se: Sempre que possível, pague o valor total da fatura!")
print("="*40 + "\n")
