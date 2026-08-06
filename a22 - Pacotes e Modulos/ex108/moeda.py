def aumentar(preco= 0, taxa= 0):
    resultado = preco + (preco * taxa/100)
    return resultado

def diminuir(preco= 0, taxa= 0):
    resultado = preco - (preco * taxa/100)

def dobro(n= 0):
    resultado = n*2
    return resultado

def metade(n = 0):
    resultado = n/2
    return resultado

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')