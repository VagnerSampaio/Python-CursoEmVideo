soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print("Entre 0 e 500 existem {} números divisiveis por 3 e a soma de todos os valores é {}".format(cont,soma))
