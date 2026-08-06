from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print("""
Suas opcoes:
[ 0 ] PEDRA
[ 1 ] Papel
[ 2 ] Tesoura
""")

computador = randint(0, 2)
jogador = int(input("Qual a sua jogada? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print("\nComputador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("jogada invalida")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("jogada invalida")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("jogada invalida")




