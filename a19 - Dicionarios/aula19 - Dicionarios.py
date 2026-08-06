#tuplas ()
#listas []
#dicionarios {}

pessoas = {"nome": "Vagner", "sexo": "M", "idade": 41}
print(pessoas)
print(pessoas["nome"])
print(pessoas["sexo"])
print(pessoas["idade"])
print(f"{pessoas['nome']} tem {pessoas['idade']} anos.")
print()

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

for key, values in pessoas.items():
    print(f"{key.capitalize()}: {values}")
print()

del pessoas["sexo"]
for key, value in pessoas.items():
    print(f"{key.capitalize()}: {value}")
print()

pessoas["nome"] = "Vagner Sampaio"
pessoas["peso"] = 84.0
for key, value in pessoas.items():
    print(f"{key.capitalize()}: {value}")
print()

brasil = list()
estado1 = {"uf":"Piaui", "sigla":"PI"}
estado2 = {"uf":"Maranhao", "sigla":"MA"}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]["sigla"])
print(brasil[1]["uf"])
print()

estado = dict()
brasil = list()

for c in range(0, 3):
    estado["uf"] = str(input("UF: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)
print()

for estado in brasil:
    print(estado)
print()

for estado in brasil:
    for key, values in estado.items():
        print(f"{key.capitalize()}: {values}")
print()

for estado in brasil:
    for values in estado.values():
        print(values,end=" ")
    print()