from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)

print("A hipotunusa vai medir {:.2f}".format(hi))

