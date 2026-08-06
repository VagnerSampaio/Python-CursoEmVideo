num = (int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),
       int(input("Digite um número: ")),)

print(f"Voce digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes")

if 3 in num:
    print(f"O valor 3 apareceu {num.index(3)+1}a posição")
else:
    print("O valor 3 não foi digitado.")

print("Os valores pares digitados foram: ", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')