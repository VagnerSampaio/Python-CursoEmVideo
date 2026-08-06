primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print("{} ".format(termo), end="")
        termo += razao
        cont += 1
    mais = int(input("\nQuantos termos voce quer mostrar a mais? "))

print("Prograssao finalizada com {} termos".format(total))