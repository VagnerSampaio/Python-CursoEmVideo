for c in range(0, 10):
    print("Ola mundo")

n = int(input("Digite um número: "))
for c in range(0, n+1):
    print(c)

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)

s = 0
for c in range(0, 4):
    n = int(input("Digite um número: "))
    s = s + n
print("O somatório é {}".format(s))