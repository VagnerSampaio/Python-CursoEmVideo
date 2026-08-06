from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "jogador1":randint(1, 6),
    "jogador2":randint(1, 6),
    "jogador3":randint(1, 6),
    "jogador4":randint(1, 6),
}

print("Valores sorteados:")
for key, value in jogo.items():
    print(f"{key} tirou o valor {value} no dado.")
    sleep(1)
print()

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("Ranking:")
for i, valor in enumerate(ranking):
    print(f"{i+1}o lugar: {valor[0]} com {valor[1]} pontos.")
