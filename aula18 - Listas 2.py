teste = list()
teste.append("Joao")
teste.append(1985)
print(teste)
print()

galera = list()
#galera.append(teste[:]) #ligação
galera.append(teste) #cópia
teste[0] = "Vagner"
teste[1] = 41
print(galera)
print()

galera = [["Joao",19],["Ana",33],["Joaquim",13],["Maria",45]]
print(galera)
print(galera[0][0])
print(galera[1])
print()

for p in galera:
    print(p)
print()

for p in galera:
    print(f"{p[0]} tem {p[1]} anos.")
print()

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 5):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1

print(f"Total de maior de idade: {totmai}"
      f"\nTotal de menor de idade: {totmen}")

