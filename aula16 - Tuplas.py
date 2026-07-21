#Tuplas ()
#Listas []
#Dicionários {}

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")

#Tuplas são imutáveis
#lanche[1] = 'Refrigerante'
print(lanche)
print(sorted(lanche)) #Ordem alfabética
print()

print(lanche[1])
print(lanche[-3])
print()

print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-2:])
print()

for comida in lanche:
    print(f"Eu vou comer {comida}.")
print()

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida}, na posicao {pos}.")
print()

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posicao {cont}.")
print()

a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
print(c)
print(d)
print(len(c))
print(c.count(5))
print(c.index(5,0)) #valor 5, começo na posição 0
print()

pessoa = ("Vagner",41,'M',1.83,82)
print(pessoa)
del pessoa
#print(pessoa)