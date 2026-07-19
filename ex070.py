total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco do produto: "))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SsNn':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break

print(f"O total da compra foi R$ {preco}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} e custa {menor}")