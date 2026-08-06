n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
opcao = 0

while opcao != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair
    """)
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        soma = n1 + n2
        print(soma)
    elif opcao == 2:
        multiplicar = n1 * n2
        print(multiplicar)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
    elif opcao == 4:
        print("Informe os numeros novamente")
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opcao invalida. Tente novamente")

