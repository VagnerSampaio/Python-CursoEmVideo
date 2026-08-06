from datetime import date

atual = date.today().year
nasc = int(input("Qual o ano de nascimento? "))

idade = atual - nasc

if idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print("Voce ainda nao pode se alistar, faltam {} anos, no ano {}".format(saldo, ano))
elif idade == 18:
    print("Voce precisa de se alistar")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("Voce deveria ter se alistado há {} anos, no ano {}".format(saldo, ano))