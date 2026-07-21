listagem = ("lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)

#print(listagem)
#for p in listagem:
#    print(f"{p} ", end=" ")

print('-'*40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print('-'*40)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f"{listagem[item]:.<30}", end=' ')
    else:
        print(f"R${listagem[item]:>7.2f}")

print("-"*40)