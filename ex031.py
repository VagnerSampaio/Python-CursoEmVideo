distancia = float(input("Qual é a distancia da viagem: "))
print("Voce esta prestes a comecar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preco da passagem será de R${:.2f}".format(preco))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45