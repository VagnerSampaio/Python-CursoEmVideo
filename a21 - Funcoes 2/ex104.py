def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print(f"\033[0;31mDigite um número inteiro valido.\033[m")
    return valor

n = leiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}")