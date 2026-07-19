from random import randint

vitorias = total = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)

    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("Par ou Impar? ")).strip().upper()[0]

    total = jogador + computador
    print(f"{jogador} + {computador} = {total}")
    print(f"Deu par" if total % 2 == 0 else f"Deu impar")

    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu")
            vitorias += 1
        else:
            print("voce perdeu")
            break
    if tipo == 'I':
        if total % 2 == 1:
            print("Você venceu")
            vitorias += 1
        else:
            print("voce perdeu")
            break
print(f"Voce venceu {vitorias} vezes.")