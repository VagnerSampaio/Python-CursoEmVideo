print("=" * 50)
print("CALCULADORA DE JUROS COMPOSTOS")
print("=" * 50)

print("\nEscolha o tipo de investimento:")
print("1 - Aporte inicial único")
print("2 - Aportes mensais recorrentes")

opcao = input("\nOpção: ")

taxa_anual = float(input("Taxa de juros anual (%): ")) / 100
anos = int(input("Tempo de investimento (anos): "))

meses = anos * 12
taxa_mensal = taxa_anual / 12

if opcao == "1":
    aporte_inicial = float(input("\nValor do aporte inicial (R$): "))

    saldo = aporte_inicial

    print("\nEvolução anual")
    print("-" * 50)

    for mes in range(1, meses + 1):
        saldo *= (1 + taxa_mensal)

        # Exibe apenas ao final de cada ano
        if mes % 12 == 0:
            ano = mes // 12
            print(f"Ano {ano:2}: R$ {saldo:,.2f}")

elif opcao == "2":
    aporte_inicial = float(input("\nAporte inicial (R$ - digite 0 se não houver): "))
    aporte_mensal = float(input("Valor do aporte mensal (R$): "))

    saldo = aporte_inicial

    print("\nEvolução anual")
    print("-" * 50)

    for mes in range(1, meses + 1):
        saldo *= (1 + taxa_mensal)
        saldo += aporte_mensal

        # Exibe apenas ao final de cada ano
        if mes % 12 == 0:
            ano = mes // 12
            print(f"Ano {ano:2}: R$ {saldo:,.2f}")

else:
    print("Opção inválida!")
    exit()

print("\n" + "=" * 50)
print(f"Valor investido: R$ {(aporte_inicial + (aporte_mensal * meses if opcao == '2' else 0)):,.2f}")
print(f"Valor final:     R$ {saldo:,.2f}")
print(f"Lucro obtido:    R$ {saldo - (aporte_inicial + (aporte_mensal * meses if opcao == '2' else 0)):,.2f}")
print("=" * 50)