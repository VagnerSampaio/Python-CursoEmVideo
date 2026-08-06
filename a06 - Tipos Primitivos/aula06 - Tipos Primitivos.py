n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
s = n1 + n2
print(type(s))

print("A soma de {} e {}, é: {}".format(n1,n2,s))


n = float(input("Digite um valor: "))
print(type(n))
print(n)


n = bool(input("Digite um valor: ")) #se tiver um valor dentro, será true
print(type(n)) #sem valor dentro = false
print(n)
print(n.is_integer())