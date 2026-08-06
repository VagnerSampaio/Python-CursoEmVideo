galera = list()
pessoa = dict()
somaidade = mediaidade = 0
while True:
    pessoa.clear()

    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! Digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    somaidade += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resp = str(input("Quer continuar [S/N]? ")).upper()[0]
        if resp in 'SN':
            break
        print("Erro! Digite apenas S ou N.")
    if resp == 'N':
        break

print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = somaidade / len(galera)
print(f"A media da idade é {media:.2f} anos.")
print(f"A mulheres cadastradas foram: ", end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"{p['nome']}, ", end='')
print()

print(f"Lista das pessoas que estão acima da média: ")
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f"{k}: {v}; ", end='')