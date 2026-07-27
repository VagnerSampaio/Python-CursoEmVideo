num = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input (f'Digite um valor: '))

    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

#num[0].sort()
#num[1].sort()

print(f'Todos valores {num}')
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores impares digitados foram: {sorted(num[1])}')