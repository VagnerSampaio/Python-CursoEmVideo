import moeda

preco = float(input("Digite o preco: R$"))
print(f"A metade de {moeda.moeda(preco, 'US$')} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro do {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}")