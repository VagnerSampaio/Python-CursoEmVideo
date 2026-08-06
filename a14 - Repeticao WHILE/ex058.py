from random import randint
computador = randint(0, 10)

print("Vou pensar em um numero entre 0 e 10")
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Em que numero eu pensei? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        if jogador > computador:
            print("Menos... Tente mais uma vez")

print("Acertou com {} tentativas".format(palpites))