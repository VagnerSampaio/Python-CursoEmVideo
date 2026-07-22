num = [2,5,9,1]
num[2] = 3
#num[4] = 7 não existe posicao [4]
num.append(7)
print(num)

num.sort()
print(num)
num.sort(reverse=True)
print(num)

num.insert(2,0) #na posicao [2] insere 0
print(num)
print(f"Essa lista tem {len(num)} elementos.")

num.pop()
print(num)

num.pop(2) #remove na posicao 2
print(num)

num.insert(2,2)
print(num)
num.remove(2) #elimina a primera ocorrencia
print(num)

if 5 in num:
    num.remove(5)
print(num)


valores = list()
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"Na posicão {c} encontrei o valor {v}!")


a = [2, 3, 4, 7]
b = a #faz uma ligação entre listas
print(f"Lista A: {a}")
print(f"Lista B: {b}")

b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")

a = [2, 3, 4, 7]
b = a[:] #faz uma cópia da lista
print(f"Lista A: {a}")
print(f"Lista B: {b}")

b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
