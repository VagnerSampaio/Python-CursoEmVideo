def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: numero a ser calculado
    :param show: (opcional) mostra o calculo do fatorial
    :return: o valor do fatorial
    """
    f = 1
    for c in range(1, n + 1):
        f *= c
        if show:
            print(c, end=" ")
            if c < n:
                print(f" x ", end=" ")
            else:
                print(" = ", end=" ")
    return f

help(fatorial)
print(fatorial(5,True))
print(fatorial(5,False))