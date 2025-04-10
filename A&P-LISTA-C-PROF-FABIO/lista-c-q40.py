anos = int(input("Anos fumando: "))
cigarros_dia = int(input("Cigarros por dia: "))
preco_carteira = float(input("Preço da carteira: "))
total_cigarros = anos * 365 * cigarros_dia
valor_total = (total_cigarros / 20) * preco_carteira
print("Total gasto:", valor_total)
