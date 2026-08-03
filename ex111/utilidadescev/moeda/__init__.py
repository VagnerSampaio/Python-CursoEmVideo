def aumentar(preco= 0, taxa= 0, formatado = False):
    """
    Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formataçao.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formatado: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formatação.
    """
    resultado = preco + (preco * taxa/100)
    return resultado if formatado is False else moeda(resultado)

def diminuir(preco= 0, taxa= 0, formatado = False):
    resultado = preco - (preco * taxa/100)
    return resultado if formatado is False else moeda(resultado)

def dobro(n= 0, formatado = False):
    resultado = n*2
    return resultado if formatado is False else moeda(resultado)

def metade(n = 0, formatado = False):
    resultado = n/2
    return resultado if formatado is False else moeda(resultado)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(preco= 0, taxa_aumento = 10, taxa_reducao = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{moeda(dobro(preco))}")
    print(f"Metade do preço: \t{moeda(metade(preco))}")
    print(f"{taxa_aumento}% de aumento: \t{moeda(aumentar(preco, taxa_aumento))}")
    print(f"{taxa_reducao}% de redução: \t{moeda(diminuir(preco, taxa_reducao))}")
    print('-' * 30)