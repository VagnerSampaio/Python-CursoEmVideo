valores = list()

while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp in "Nn":
        break

print("-=" * 30)
print(f"Voce digitou {len(valores)} elementos")

valores.sort(reverse=True)
print(f"Ordem decrescente da lista de valores: {valores}")

if 5 in valores:
    print("O valor 5 apareceu na lista")
else:
    print("O valor 5 não apareceu na lista")