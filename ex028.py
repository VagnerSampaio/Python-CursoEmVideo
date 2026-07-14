from random import randint
computador = randint(0, 5)

jogador = int(input('Em que jogo eu pensei? '))

if jogador == computador:
    print("Parabens! Voce venceu! Pensei: {}".format(computador))
else:
    print("Ganhei! Voce perdeu! Pensei: {}".format(computador))