preco = float(input("Preco das compras R$ "))
print("""Forma de pagamento:
[1] a vista dinheiro
[2] a vista cartao
[3] 2x no cartao
[4] 3x no cartao""")
opcao = int(input("Qual a opcao? "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela = total / 3
else:
    total = 0
    print("Opcao invalida")

print("Sua compra de R${:.2f} vai custar R${:.2f}".format(preco, total))