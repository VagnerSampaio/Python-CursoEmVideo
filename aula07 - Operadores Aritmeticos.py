n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divi = n1 // n2
exp = n1 ** n2

print("Operações:\nA soma de é {}, o produto é {}, e a divisão é {:.2f}".format(soma, mult, div), end=", ")
print("a divisão inteira {} e potência {}.".format(divi, exp))

#5+2 == 7
#5-2 == 3
#5*2 == 10
#5/2 == 2.5
#5**2 == 25
#5//2 == 2
#5%2 == 1

#Ordem de Precedência
#1. ()
#2. **
#3. *, /, //, %
#4. +, -

#5 + 3 * 2 = 5 + 6 = 11
#3 * 5 + 4 ** 2 = 3 * 5 + 16 = 15 + 16 = 31
#3 * (5 + 4) ** 2 = 3 * (9) ** 2 = 3 * 81 = 243

nome = input("\nDigite seu nome: ")
print("Prazer em te conhecer {:20}!".format(nome)) #20 caracteres
print("Prazer em te conhecer {:>20}!".format(nome)) #direita
print("Prazer em te conhecer {:<20}!".format(nome)) #esquerda
print("Prazer em te conhecer {:^20}!".format(nome)) #centralizado
print("Prazer em te conhecer {:=^20}!".format(nome)) #com preenchimento