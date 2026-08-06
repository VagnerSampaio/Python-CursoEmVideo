import moeda

preco = float(input("Digite o preco: R$"))
print(f"A metade de {preco} é {moeda.metade(preco)}")
print(f"O dobro do {preco} é {moeda.dobro(preco)}")
print(f"Aumentando em 10%, temos {moeda.aumentar(preco, 10)}")