def ficha(nome='<desconhecido>',gols=0):
    print(f"O jogador {nome} fez {gols} gol(s)")

nome = str(input("Nome do jogador: "))
gols = str(input("Gols no campeonato: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    ficha(gols=gols)
else:
    ficha(nome,gols)