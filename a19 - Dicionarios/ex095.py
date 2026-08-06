time = list()
jogador = dict()
partidas = list()


while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c+1}? ")))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == "N":
        break
print()

print("Cod ", end="")
for i in jogador.keys():
    print(f"{i:<15} ", end="")
print()
for k, v in enumerate(time):
    print(f"{k:>3}", end=" ") #codigo jogador
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print()

while True:
    busca = int(input("Mostrar dados de qual jogador? [999 = break] "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro! Não existe jogador com codigo {busca}.")
    else:
        print(f"Jogador {time[busca]['nome'].upper()}")
        for i, gols in enumerate(time[busca]["gols"]):
            print(f"    => Na partida {i+1}, fez {gols} gols.")
print()