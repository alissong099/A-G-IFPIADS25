def calcular_cdb(valor_investido, taxa_anual, anos):
    montante = valor_investido * (1 + taxa_anual / 100) ** anos
    return montante


def calcular_cdc(valor_emprestado, taxa_mensal, meses):
    taxa_decimal = taxa_mensal / 100
    parcela = (valor_emprestado * taxa_decimal * (1 + taxa_decimal) ** meses) / ((1 + taxa_decimal) ** meses - 1)
    montante_total = parcela * meses
    juros_totais = montante_total - valor_emprestado
    return parcela, montante_total, juros_totais


# Entrada de dados

valor = float(input('Informe o valor para investimento/empréstimo: '))
anos_cdb = int(input('Informe o prazo do CDB (em anos): '))
taxa_cdb = float(input('Informe a taxa anual do CDB (entre 1% e 20%): '))

meses_cdc = int(input('Informe o prazo do CDC (24, 36 ou 60 meses): '))
taxa_cdc = float(input('Informe a taxa mensal do CDC (entre 1% e 17%): '))

# Cálculo do CDB

montante_cdb = calcular_cdb(valor, taxa_cdb, anos_cdb)
juros_cdb = montante_cdb - valor

# Cálculo do CDC

parcela_cdc, montante_cdc, juros_cdc = calcular_cdc(valor, taxa_cdc, meses_cdc)

# Lucro do banco

lucro_banco = juros_cdc - juros_cdb

# Exibição dos resultados
print("\n=== SIMULAÇÃO CDB ===")
print(f"Valor investido: R$ {valor:.2f}")
print(f"Taxa anual: {taxa_cdb}%")
print(f"Prazo: {anos_cdb} anos")
print(f"Montante final: R$ {montante_cdb:.2f}")
print(f"Juros pagos pelo banco: R$ {juros_cdb:.2f}")

print("\n=== SIMULAÇÃO CDC ===")
print(f"Valor emprestado: R$ {valor:.2f}")
print(f"Taxa mensal: {taxa_cdc}%")
print(f"Prazo: {meses_cdc} meses")
print(f"Parcela mensal: R$ {parcela_cdc:.2f}")
print(f"Montante total pago pelo cliente: R$ {montante_cdc:.2f}")
print(f"Juros pagos pelo cliente: R$ {juros_cdc:.2f}")

print("\n=== LUCRO DO BANCO ===")
print(f"Lucro obtido: R$ {lucro_banco:.2f}")