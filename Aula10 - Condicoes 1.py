from selectors import SelectSelector

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")

print("Carro novo" if tempo <= 3 else "Carro velho")

print("--Fim--")


nome = str(input('Qual o seu nome? '))
print("Bom dia, {}".format(nome))
if nome == "Vagner":
    print("Que nome lindo você tem!")
else:
    print("Seu nome é tão normal!")

n1 = int(input('Qual o primeiro valor? '))
n2 = int(input('Qual o segundo valor? '))
media = (n1 + n2) / 2
print("Sua média foi {:.2}".format(media))
if media >= 7:
    print("Aprovado")
else:
    if media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")