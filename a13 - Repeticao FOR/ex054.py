from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nasc = int(input("Qual o ano de nascimento? "))
    idade = atual - nasc

    if idade >= 18:
        print("Maior de idade")
        totmaior += 1
    else:
        print("Menor de idade")
        totmenor += 1

print("Ao todo tivemos {} pessoas maiores de idade e {} pessoas menor de idade".format(totmaior, totmenor))