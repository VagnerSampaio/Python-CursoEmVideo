print('-'*40)
print(f'{"Curso em vídeo":^40}')
print('-'*40)
print()

def linha():
    print('-'*40)
linha()
print(f'{"Curso em vídeo":^40}')
linha()
print()

def titulo(texto):
    linha()
    print(f'{texto:^40}')
    linha()
titulo("Faculdade PIT")
titulo("Algoritmos com Python")
titulo("Prof. Vagner")
print()

def soma(a, b):
    soma = a + b
    print(f"A soma de {a} e {b} é {soma}")
soma(19,85)
soma(a=4,b=5)
soma(b=2,a=9)
print()

def contador(*numeros): #empacotador em Tuplas
    tamanho = len(numeros)
    print(f"Recebi os numeros {numeros} e ao todo sao {tamanho}")
    for c in range(0, len(numeros)):
        print(numeros[c], end=' ')
    print()

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
print()

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1
    print(lista)
    print()

valores = [6,3,9,1,0,2]
valores.append(7)
dobra(valores)

def soma2(*valores):
    soma = 0
    for v in valores:
        soma += v
    print(soma)
    print()

soma2()
soma2(5,2)
soma2(2,9,4)
soma2(19,2,1985)