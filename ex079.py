numeros = list()

while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado!")

    resp = str(input("Deseja continuar? [S/N] ")).upper().split()[0]
    if resp in "Nn":
        break

print("-=" * 30)
numeros.sort()
print(f"Voce digitou os valores {numeros}")