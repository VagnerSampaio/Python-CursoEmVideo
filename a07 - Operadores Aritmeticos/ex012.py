valor = float(input("Qual o valor do produto? "))
novo = valor - (valor * 5 / 100)

print("O produto custava R${}, na promoção com desconto de 5% vai custar R${}".format(valor, novo))