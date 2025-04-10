def calcular_combustivel(distancia, percentual_eletrico, consumo_gasolina, consumo_alcool, preco_gasolina, preco_alcool):
    # Parte da viagem que será feita com motor a combustão
    distancia_combustao = distancia * (1 - percentual_eletrico / 100)

    # Cálculo de litros necessários
    litros_gasolina = distancia_combustao / consumo_gasolina
    litros_alcool = distancia_combustao / consumo_alcool

    # Cálculo de custos
    custo_gasolina = litros_gasolina * preco_gasolina
    custo_alcool = litros_alcool * preco_alcool

    return litros_gasolina, custo_gasolina, litros_alcool, custo_alcool

# Entradas
print("=== PLANEJAMENTO DE VIAGEM - CARRO HÍBRIDO ===")
distancia = float(input("Informe a distância total da viagem (em km): "))
preco_gasolina = float(input("Informe o preço do litro da gasolina (R$): "))
preco_alcool = float(input("Informe o preço do litro do álcool (R$): "))
percentual_eletrico = float(input("Informe o percentual (%) da viagem com motor elétrico: "))

# Consumo padrão
consumo_gasolina = 12  # km/l
consumo_alcool = consumo_gasolina * 0.8  # 80% do consumo da gasolina

# Cálculos
litros_gasolina, custo_gasolina, litros_alcool, custo_alcool = calcular_combustivel(
    distancia, percentual_eletrico, consumo_gasolina, consumo_alcool, preco_gasolina, preco_alcool
)

# Saída
print("\n=== TABELA COMPARATIVA DE CUSTOS ===")
print(f"Distância total da viagem: {distancia} km")
print(f"Percentual com motor elétrico: {percentual_eletrico}%")
print(f"Distância com motor a combustão: {distancia * (1 - percentual_eletrico / 100):.2f} km")

print("\nCom Gasolina:")
print(f"- Litros necessários: {litros_gasolina:.2f} L")
print(f"- Custo total: R$ {custo_gasolina:.2f}")

print("\nCom Álcool:")
print(f"- Litros necessários: {litros_alcool:.2f} L")
print(f"- Custo total: R$ {custo_alcool:.2f}")
