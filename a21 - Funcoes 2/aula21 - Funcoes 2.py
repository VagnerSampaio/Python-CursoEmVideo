#help() no console
from operator import truediv

help(print)
print()
print(input.__doc__)
print()

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno
    Função criada por Vagner Sampaio.
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += 1

contador(2,10,2)
print()

help(contador)
print()

def somar(a=0, b=0,c =0): # a,b,c=0 é parametro opcional
    s = a + b + c
    print(f"A soma vale {s}")

somar(3,2,5)
somar(8,4)
somar()
print()

def teste():
    x = 8 #variavel local
    print(f"Na funcao teste, n vale {n}")
    print(f"Na funcao teste, x vale {x}")

n = 2 #variavel global
print(f"No programa principal, n vale {n}")
teste()
print()

def teste(b):
    global a #variavel global, afeta fora da funcao
    a = 8
    b += 4 #variavel local
    c = 2 #variavel local
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5
teste(a)
print(f"A fora vale {a}")
print()

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(8,4)
r3 = somar(4)

print(f"Os resultados das somas foram: {r1}, {r2} e {r3}.")
print()

def fatorial(n=1):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f

f5 = fatorial(5)
f3 = fatorial(3)
f1 = fatorial(1)

print(f"Os fatoriais são: {f1}, {f3} e {f5}")
print()

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {fatorial(n)}")

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

if par(n):
    print("Par")
else:
    print("Impar")

print()